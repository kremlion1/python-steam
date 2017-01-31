from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
app = Flask(__name__)
games = ('game1', 'game2')


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=80, host='192.168.1.144')


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)

    return jsonify({'game': games[0], 'action': 'get'}), 201
