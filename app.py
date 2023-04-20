from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/move_character', methods=['POST'])
def move_character():
    data = request.get_json()
    x_position = data.get('x_position')
    y_position = data.get('y_position')

    # Process the new character position in your game logic here.

    response = {
        'status': 'success',
        'message': 'Character moved successfully.',
        'x_position': x_position,
        'y_position': y_position
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
