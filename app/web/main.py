from app.config import test
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = test.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = test.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)  # SQLAlchemy 객체는 앱 컨텍스트와 함께 싱글톤처럼 동작

# # 환경 변수로 환경에 맞는 설정 파일 로드
# app.config.from_object(f"configs.{os.getenv('FLASK_ENV', 'dev')}")

 
@app.route("/DS18b20.json")
def DS18b20():
    cursor.execute("SELECT Date, wTemp from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/DHT22T.json")
def DHT22T():
    cursor.execute("SELECT Date, Temp from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/DHT22H.json")
def DHT22H():
    cursor.execute("SELECT Date, Hum from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/MH_Z19CO2.json")
def MH_Z19CO2():
    cursor.execute("SELECT Date, Co2 from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/MH_Z19T.json")
def MH_Z19T():
    cursor.execute("SELECT Date, CoTemp from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/MQ2GAS.json")
def MQ2GAS():
    cursor.execute("SELECT Date, Gas from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

@app.route("/GY_712C.json")
def GY_712C():
    cursor.execute("SELECT Date, Current from datas")
    results = cursor.fetchmany(150)
    return json.dumps(results)

 
 #플라스크 이용해 그래프로 출력
@app.route("/DS18b20") 
def DS18b20graph():
    return render_template('templates/DS18b20.html')

@app.route("/DHT22T") 
def DHT22Tgraph():
    return render_template('templates/DHT22T.html')

@app.route("/DHT22H") 
def DHT22Hgraph():
    return render_template('templates/DHT22H.html')

@app.route("/MH_Z19T") 
def MH_Z19Tgraph():
    return render_template('templates/MH_Z19T.html')

@app.route("/MH_Z19CO2") 
def MH_Z19CO2graph():
    return render_template('templates/MH_Z19CO2.html')
 
@app.route("/MQ2GAS") 
def MQ2GASgraph():
    return render_template('templates/MQ2GAS.html')

@app.route("/GY_712C") 
def GY_712Cgraph():
    return render_template('templates/GY_712C.html')


@app.route("/")
def home():
    return render_template('templates/home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)


"""
2. Flask 기본 구조에서 싱글톤 적용 여부
Flask와 WSGI의 작동 방식

Flask는 기본적으로 싱글톤처럼 작동한다. 앱 객체(Flask app)는 한 번만 생성되고 WSGI 서버에 의해 관리된다.
즉, Flask 애플리케이션 자체가 싱글톤 역할을 한다. 대부분의 경우 추가적인 싱글톤 구현 없이 Flask 객체와 확장(extension)을 활용하면 충분하다.

플라스크의 확장 관리
Flask 확장(예: Flask-SQLAlchemy, Flask-Caching)은 보통 애플리케이션 컨텍스트와 함께 동작하며, 싱글톤처럼 공유된다.

# Flask는 application context와 request context를 사용해 전역 변수를 관리할 수 있다.
"""