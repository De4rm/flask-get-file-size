from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired


class FileForm(FlaskForm):
	file_upload = FileField("Browse...", validators=[FileRequired()])
	submit = SubmitField("Submit Query")