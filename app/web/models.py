from app.web.main import db

class Data(db.Model):
    __tablename__ = 'IOT_RAW_DATAS'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    w_temp = db.Column(db.Float)
    temp = db.Column(db.Float)
    hum = db.Column(db.Float)
    co2 = db.Column(db.Float)
    co_temp = db.Column(db.Float)
    gas = db.Column(db.Float)
    current = db.Column(db.Float)
