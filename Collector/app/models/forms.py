from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    InitialDate = StringField("InitialDate", validators=[DataRequired()])
    FinalDate = StringField("FinalDate")