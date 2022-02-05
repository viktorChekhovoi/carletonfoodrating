from app import db

class DiningHall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    #station1 = db.Column(db.String(128), unique=True)
    #station2 = db.Column(db.String(128), unique=True)
    #station3 = db.Column(db.String(128), unique=True)
    #station4 = db.Column(db.String(128), unique=True)
    #station5 = db.Column(db.String(128), unique=True)
    #station6 = db.Column(db.String(128), unique=True)

    stations = db.relationship('Station', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Dining Hall>'


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    #food = db.Column(db.Text)
    locationId = db.Column(db.Integer, db.ForeignKey('dining_hall.id'))

    foods = db.relationship('Food', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Station>'


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    rating = db.Column(db.Float)
    stationId = db.Column(db.Integer, db.ForeignKey('station.id'))

    def __repr__(self):
        return f'{self.name} is rated {self.rating} our of 10'
