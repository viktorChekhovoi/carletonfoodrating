from app import db

class DiningHall(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=False)
    stations = db.relationship('Station', backref='hall', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Dining Hall with id {self.id}>'


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    locationId = db.Column(db.Integer, db.ForeignKey(DiningHall.id))

    foods = db.relationship('Food', backref='station_location', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Station with id {self.id}>'


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    rating = db.Column(db.Float)
    stationId = db.Column(db.Integer, db.ForeignKey('station.id'))

    def __repr__(self):
        return f'{self.name} is rated {self.rating} our of 10 with id {self.id}'
