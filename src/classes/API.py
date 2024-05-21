from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def receive_json():
    # Recibir el JSON enviado por POST
    data = request.json

    # Puedes procesar o imprimir el JSON recibido aquí
    print("Received JSON:", data)

    # Responder con código 200 y un mensaje JSON
    return jsonify("OK"), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
