from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,SelectField,IntegerField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class SubmitPitch(FlaskForm):
    post = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('About Pitch', validators=[DataRequired()])
    category = SelectField('Pick Category', choices=[('Interview', 'Interview'),('Product', 'Product'),('Promotion', 'Promotion')])
    user_id = IntegerField('User Id', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):

    title = StringField('title',validators=[DataRequired()])

    comment = TextAreaField('Pitch Comment', validators=[DataRequired()])

    submit = SubmitField('Submit')