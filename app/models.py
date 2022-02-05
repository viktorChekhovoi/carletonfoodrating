from app import db

class DiningHall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    station1 = db.column(db.String(128), unique=True)
    station2 = db.column(db.String(128), unique=True)
    station3 = db.column(db.String(128), unique=True)
    station4 = db.column(db.String(128), unique=True)
    station5 = db.column(db.String(128), unique=True)
    station6 = db.column(db.String(128), unique=True)

    def __repr__(self):
        return f'<{self.name} Dining Hall>'


class Station(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    food = db.Column(db.Text)

    def __repr__(self):
        return f'<{self.name} Station>'


class Food(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'{self.name} is rated {self.rating} our of 10'
