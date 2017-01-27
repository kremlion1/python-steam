from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
import psycopg2
app = Flask(__name__)
games = ('game1', 'game2')


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    connect = psycopg2.connect(database='steam_base', user='test_user', host='localhost', password='test_password')
    cursor = connect.cursor()

    #cursor.execute("CREATE TABLE tbl(id INT, data JSON);")

    #cursor.execute('INSERT INTO tbl VALUES (1, \'{ "name":"Tester" }\');')
    #connect.commit()

    cursor.execute("SELECT * FROM tbl;")
    for row in cursor:
        print(row)

    connect.close()
    app.run(port=80)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)

    return jsonify({'game': games[0], 'action': 'get'}), 201
