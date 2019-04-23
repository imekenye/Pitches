from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class SubmitPitch(FlaskForm):
    post = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('About Pitch', validators=[DataRequired()])
    category = StringField('What category is it?', validators=[DataRequired()])
