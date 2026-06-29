import os
from flask import Flask, request
from markupsafe import escape
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Control 1: clave secreta desde variable de entorno
app.secret_key = os.getenv("SECRET_KEY", "clave_temporal_laboratorio")

# Control 2: contraseña desde variable de entorno
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "cambiar_en_entorno")


@app.route("/")
def inicio():
    nombre = request.args.get("nombre", "")

    # Control 3: escape de datos ingresados por el usuario
    nombre_seguro = escape(nombre)

    return f"<h1>Bienvenido {nombre_seguro}</h1>"


@app.route("/login")
def login():
    password = request.args.get("password", "")

    if password == ADMIN_PASSWORD:
        return "Acceso concedido"

    return "Acceso denegado"


if __name__ == "__main__":
    # Control 4: debug desactivado
    app.run(debug=False)