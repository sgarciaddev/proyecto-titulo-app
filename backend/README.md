# Proyecto de título - App (backend)

<div align="center">

[![python-badge]][python-web] [![venv-badge]][pyenv-web]

[![flask-badge]][flask-web] [![pycharm-badge]][pycharm-web]

</div>

Microservicio de Python/Flask con la API Rest que es consumida por la
aplicación de Vue.js, y se encarga de mostrar los resultados obtenidos en
las pruebas de mitigación hechas a los modelos de aprendizaje automático
entrenados previamente.

## Requisitos

- [Python](https://www.python.org/) v3.10
- [Pip](https://pypi.org/project/pip/)

## Instalación

Para ejecutar este proyecto, es necesario seguir los siguientes pasos:

1. Crear un entorno virtual de Python 3.10 en el directorio `backend`.

    ```bash
    cd backend && python3.10 -m venv
    ```

2. Instalar las dependencias del proyecto

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecutar el servidor de Flask

    ```bash
    python app.py
    ```

4. Acceder a la URL `http://localhost:5000`, que servirá como ENDPOINT de la API
   Rest.

## Librerías externas

- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Framework de Python
  para el desarrollo de aplicaciones web, utilizada para la creación de la API
  Rest.
- [python-dotenv](https://pypi.org/project/python-dotenv/): Librería de Python
  que permite cargar variables de entorno desde un archivo `.env`.

## Endpoints

### Ruta `/`

#### `GET /`

- **Descripción**: Retorna un mensaje de bienvenida.
- **Params:** Ninguno
- **Respuesta:** Mensaje de bienvenida (`application/json`)
- **Códigos de estado:**
    - `200`: Mensaje de bienvenida
    - `500`: Error interno del servidor

### Ruta `/simulate`

#### `POST /simulate`

- **Descripción**: Genera una simulación de mitigación de ataques DDoS
  a un modelo de aprendizaje automático.
- **Params:** Ninguno
- **Body:** Datos de la simulación (`application/json`)
    - `model`: Modelo de aprendizaje automático a simular
    - `dataset`: Set de datos a simular
    - `attack_size`: Cantidad de ataques a simular (paquetes de red)
- **Respuesta:** Matriz de confusión (`application/json`)
- **Códigos de estado:**
    - `200`: Ok. Matriz de confusión generada
    - `400`: Parámetros/body inválidos
    - `500`: Error interno del servidor

<!-- badges -->

[python-badge]: https://img.shields.io/badge/Python%203.10-3776AB?logo=python&logoColor=FFF&style=flat

[python-web]: https://www.python.org/

[venv-badge]: https://img.shields.io/badge/Virtualenv-4B8BBE?logo=python&logoColor=FFF&style=flat

[pyenv-web]: https://virtualenv.pypa.io/en/latest/

[flask-badge]: https://img.shields.io/badge/Flask-000?logo=flask&logoColor=FFF&style=flat

[flask-web]: https://flask.palletsprojects.com/en/2.0.x/

[pycharm-badge]: https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=FFF&style=flat

[pycharm-web]: https://www.jetbrains.com/pycharm/