from flask import Flask, request

app = Flask(__name__)

# Riesgo 1: clave secreta escrita directamente en el código
app.secret_key = "clave_secreta_123"

# Riesgo 2: contraseña hardcodeada
ADMIN_PASSWORD = "admin123"


@app.route("/")
def inicio():
    nombre = request.args.get("nombre", "")

    # Riesgo 3: se muestra una entrada del usuario sin validación ni escape
    return f"<h1>Bienvenido {nombre}</h1>"


@app.route("/login")
def login():
    password = request.args.get("password", "")

    if password == ADMIN_PASSWORD:
        return "Acceso concedido"

    return "Acceso denegado"


if __name__ == "__main__":
    # Riesgo 4: modo debug activo
    app.run(debug=True)
    