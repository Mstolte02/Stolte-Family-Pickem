from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class PickForm(FlaskForm):
    pick = SelectField("Pick the winner:", validators=[DataRequired()])
    submit = SubmitField("Submit Pick")
