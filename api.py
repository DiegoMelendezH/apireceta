from flask import Flask, request, jsonify

app = Flask(__name__) 

#Base de datos simulada de recetas
recetas = []

#Endpoint para agregar una nueva receta
@app.route('/recetas', methods=['POST'])
def agregar_receta():
    nueva_receta = request.json
    recetas.append(nueva_receta)
    return jsonify({'message': 'Receta agregada correctamente'}), 201

#Endpoint para obtener todas las recetas
@app.route('/recetas', methods=['GET'])
def obtener_recetas():
    return jsonify(recetas)

#Endpoint para obtener detalle de una receta especifica
@app.route('/recetas/<int:id>', methods=['GET'])
def obtener_receta(id):
    for receta in recetas:
        if receta['id'] == id:
            return jsonify(receta)
    return jsonify({'message': 'Receta no encontrado'}), 404

@app.route('/recetas/<int:id>', methods=['PUT'])
def actualizar_receta(id):
    for receta in recetas:
        if receta['id'] == id:
            receta_actualizada = request.json
            receta.update(receta_actualizada)
            return jsonify({'message': 'Receta actualizada correctamente'})
    return jsonify({'message': 'Receta no encontrada'}), 404

# Endpoint para eliminar una receta existente
@app.route('/recetas/<int:id>', methods=['DELETE'])
def eliminar_receta(id):
    for receta in recetas:
        if receta['id'] == id:
            recetas.remove(receta)
            return jsonify({'message': 'Receta eliminada correctamente'})
    return jsonify({'message': 'Receta no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)