from flask import jsonify, request
from models.gato import Gato
from models.perro import Perro
from models.huron import Huron
from models.boa import Boa

animales = {
    "gato": Gato,
    "perro": Perro,
    "huron": Huron,
    "boa": Boa
}

def obtener_animal_por_tipo():
    """Controlador para devolver información de un animal según el tipo."""
    tipo = request.args.get('tipo')  # Leer parámetro 'tipo' del query string
    if tipo in animales:
        return jsonify(animales[tipo].obtener_sonido())
    return jsonify({"error": "Animal no encontrado"}), 404

animales = {
    "gato": Gato,
    "perro": Perro,
    "huron": Huron,
    "boa": Boa
}

def obtener_animal(nombre):
    """Controlador para obtener un animal por nombre"""
    if nombre in animales:
        return jsonify(animales[nombre].obtener_sonido())
    return jsonify({"error": "Animal no encontrado"}), 404

def agregar_animal(data):
    """Controlador para agregar un nuevo animal (no implementado dinámicamente en este ejemplo)"""
    return jsonify({"error": "Función no implementada"}), 501
