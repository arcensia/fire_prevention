from models import IotDatas, db
from app.web.utils import utils

SENSOR_COLUMNS = {
    "DS18b20": IotDatas.w_temp,
    "DHT22T": IotDatas.temp,
    "DHT22H": IotDatas.hum,
    "MH_Z19CO2": IotDatas.co2,
    "MH_Z19T": IotDatas.co_temp,
    "MQ2GAS": IotDatas.gas,
    "GY_712C": IotDatas.current,
}

def get_sensor_data(sensor):
    if sensor not in SENSOR_COLUMNS:
        return None
    return IotDatas.query.with_entities(IotDatas.date, SENSOR_COLUMNS[sensor]).order_by(IotDatas.date.desc()).limit(150).all()


def insert_test_data():
    csv_file_path = "/Users/kim-yeonghyeon/PycharmProjects/fire_prevention/app/web/utils/datas2.csv"
    records = utils.insert_csv_data(csv_file_path=csv_file_path)
    db.session.bulk_save_objects(records)
    db.session.commit()

    # 데이터 확인 (개발용)
    results = IotDatas.query.all()
