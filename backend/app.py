from flask import Flask, jsonify
from os import getenv
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    print(getenv('EXAMPLE'))
    app.run(debug=True)
