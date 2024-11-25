from flask import Flask, render_template
from controllers.animal_controller import obtener_animal

# Configuración de la aplicación
app = Flask(__name__, template_folder='views')

# Rutas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/animal/<nombre>', methods=['GET'])
def get_animal(nombre):
    return obtener_animal(nombre)

if __name__ == '__main__':
    app.run(debug=True)
