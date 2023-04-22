from flask import Flask, jsonify, request, render_template
from char_logic import Character
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

character = Character()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/spawn_object', methods=['POST'])
def api_spawn_object():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')

    if x is not None and y is not None:
        character.spawn_object(x, y)
        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Invalid coordinates")

@app.route('/api/get_objects', methods=['GET'])
def api_get_objects():
    objects = character.get_objects()
    return jsonify(objects)

if __name__ == '__main__':
    app.run(debug=True)
