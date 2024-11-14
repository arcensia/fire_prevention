from flask import Flask, render_template, request
#import sqlite3
import mariadb
import sys
import json
 
app = Flask(__name__)

# Connect to MariaDB Platform
conn = mariadb.connect(
    user="root",
    password="root",
    host="localhost",
    database="firepre1"
)
cursor = conn.cursor()
 
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

@app.route("/")
def home():
    return render_template('templates/home.html')
 
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)