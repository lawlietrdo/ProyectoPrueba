from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

# Crear la app Flask
app = Flask(__name__)

# Configurar la conexión a MongoDB
MONGO_URI = "mongodb+srv:"
client = MongoClient(MONGO_URI)
db = client['ACMEINC']  # Cambia al nombre real de tu base de datos
collection = db['data']  # Cambia al nombre de tu colección

@app.route('/')
def home():
    return jsonify({"message": "¡Bienvenido a tu API Flask con MongoDB Atlas!"})

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)})

@app.route('/get', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == '__main__':
    # Inserción directa desde Python (fuera de Flask):
    documento = {
        "nombre": "Luis777",
        "edad": 30,
        "ocupacion": "Desarrollador",
        "habilidades": ["Python", "MongoDB", "Flask"]
    }
    # Insertar el documento
    resultado = collection.insert_one(documento)
    print(f"Documento insertado con ID: {resultado.inserted_id}")

    # Ejecutar la aplicación Flask
    app.run(debug=True)
