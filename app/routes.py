# app/routes.py
from flask import render_template, jsonify
from app import app
from app.models import ClockModel

# Creamos una instancia única del modelo del reloj
clock_model = ClockModel()

@app.route('/')
def index():
    """Sirve la página principal del reloj."""
    # Flask buscará automáticamente 'index.html' en la carpeta 'templates'
    return render_template('index.html')

@app.route('/time')
def get_time():
    """API endpoint que devuelve la hora actual."""
    hour_node, minute_node, second_node = clock_model.get_current_time_nodes()
    
    current_time = {
        "hour": hour_node.data,
        "minute": minute_node.data,
        "second": second_node.data,
        "next_second": second_node.next.data
    }
    return jsonify(current_time)