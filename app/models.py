from app import db

class DiningHall(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), index=True)
    stations = db.relationship('Station', backref='hall', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Dining Hall with id {self.id}>'


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    locationId = db.Column(db.Integer, db.ForeignKey("dining_hall.id"))

    foods = db.relationship('Food', backref='station_location', lazy='dynamic')

    def __repr__(self):
        return f'<{self.name} Station with id {self.id}>'


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    averate_rating = db.Column(db.Float, default=1.5, nullable=False)
    stationId = db.Column(db.Integer, db.ForeignKey('station.id'))
    def __repr__(self):
        return f'<{self.name} Food with rating {self.averate_rating}>'

    ratings = db.relationship('Rating', backref='foodRated', lazy='dynamic')


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    food_rated = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __repr__(self):
        return f'{self.name} is rated {self.rating} our of 10 with id {self.id}'
