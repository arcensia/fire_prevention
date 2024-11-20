import csv
from datetime import datetime
from models import IotDatas

def insert_csv_data(csv_file_path):
    records = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # 헤더 건너뛰기
        for row in csv_reader:
            records.append(IotDatas(
                date=datetime.strptime(row[0], '%Y-%m-%d %H:%M'),
                w_temp=float(row[1]),
                temp=float(row[2]),
                hum=float(row[3]),
                co2=float(row[4]),
                co_temp=float(row[5]),
                gas=float(row[6]),
                current=float(row[7]),
            ))
    return records
