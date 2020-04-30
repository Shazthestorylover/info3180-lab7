from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Email

class ProfileForm(FlaskForm):
    description = TextAreaField('Description', validators = [DataRequired()])
    photo = FileField('ProfilePic', validators = [FileRequired(),FileAllowed(['jpg','png','jpeg','Images only!'])])
