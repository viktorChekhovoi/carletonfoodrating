from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RateForm(FlaskForm):
    rating = IntegerField('Your Rating:', validators=[NumberRange(min=0, max=10), DataRequired()])
    submit = SubmitField('Submit')