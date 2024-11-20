from flask import Flask, render_template, jsonify
from config import test
import service
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = test.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = test.SQLALCHEMY_TRACK_MODIFICATIONS

# 데이터베이스 초기화
db.init_app(app)

@app.before_request
def setup_database():
    db.create_all()  # 테이블 생성

@app.route("/sensor/<sensor>.json")
def get_sensor_data(sensor):
    results = service.get_sensor_data(sensor)
    if results is None:
        return jsonify({"error": "Invalid sensor"}), 404
    return jsonify(results)

@app.route("/sensor/<sensor>")
def get_sensor_graph(sensor):
    return render_template(f'{sensor}.html')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/addData")
def add_data():
    service.insert_test_data()
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
