from os import getenv
from os.path import join as path_join

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request

load_dotenv()
if not getenv('DATA_SOURCE_PATH'):
    raise EnvironmentError('La variable de entorno DATA_SOURCE_PATH no esta definida')
if not getenv('TRAINED_MODELS_PATH'):
    raise EnvironmentError('La variable de entorno TRAINED_MODELS_PATH no esta definida')

app = Flask(__name__)

# Modelos entrenados
models = {
    'rf': {
        'cicddos2019': joblib.load(path_join(getenv('TRAINED_MODELS_PATH'), 'CICDDOS2019-RF.joblib')),
        'nbaiot': joblib.load(path_join(getenv('TRAINED_MODELS_PATH'), 'NBAIOT-RF.joblib')),
    },
    'xgb': {
        'cicddos2019': joblib.load(path_join(getenv('TRAINED_MODELS_PATH'), 'CICDDOS2019-XGB.joblib')),
        'nbaiot': joblib.load(path_join(getenv('TRAINED_MODELS_PATH'), 'NBAIOT-XGB.joblib')),
    },
    'lstm': {
        'cicddos2019': tf.keras.models.load_model(path_join(getenv('TRAINED_MODELS_PATH'), 'CICDDOS2019-LSTM.h5')),
        'nbaiot': tf.keras.models.load_model(path_join(getenv('TRAINED_MODELS_PATH'), 'NBAIOT-LSTM.h5'))
    },
}


def load_dataset(dataset_name):
    dataset_path = path_join(getenv('DATA_SOURCE_PATH'), f'{dataset_name}.csv')
    data = pd.read_csv(dataset_path)
    return data


def compute_confusion_matrix(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    return TP, FP, TN, FN


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/simulate', methods=['POST'])
def attack_simulation():
    data = request.get_json()
    dataset_name = data['dataset']
    model_name = data['model']
    attack_size = int(data['attack_size'])

    # Validamos que el body de la petición tenga los campos requeridos
    if 'dataset' not in data or 'model' not in data or 'attack_size' not in data:
        return jsonify({'error': 'Los campos dataset, model y attack_size son requeridos'}), 400

    # Validamos que los valores de los campos sean válidos
    if dataset_name not in ['cicddos2019', 'nbaiot']:
        return jsonify({'error': 'El valor del campo dataset no es válido'}), 404
    if model_name not in ['rf', 'xgb', 'lstm']:
        return jsonify({'error': 'El valor del campo model no es válido'}), 404
    if 0 <= attack_size <= 500000:
        return jsonify({'error': 'El valor del campo attack_size no es válido'}), 404

    dataset = load_dataset(dataset_name)
    sample_data = dataset.sample(n=attack_size)

    X = sample_data.drop('Label', axis=1)
    y_true = sample_data['Label'].values

    y_pred = models[model_name][dataset_name].predict(X)
    y_pred_binary = (y_pred > 0.5).astype(int)

    TP, FP, TN, FN = compute_confusion_matrix(y_true, y_pred_binary)

    return jsonify({'TP': int(TP), 'FP': int(FP), 'TN': int(TN), 'FN': int(FN)})


if __name__ == '__main__':
    app.run(debug=True)
