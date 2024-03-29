from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange


class RateForm(FlaskForm):
    name = ""
    rating = IntegerField(
        "Your Rating:", validators=[NumberRange(min=0, max=10), DataRequired()]
    )
    submit = SubmitField("Submit")
