# app/__init__.py
from flask import Flask

# Se crea la instancia de la aplicación
app = Flask(__name__)

# Se importan las rutas para que Flask las conozca
from app import routes
