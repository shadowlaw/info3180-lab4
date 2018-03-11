from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import allowed_uploads

class UploadForm(FlaskForm):
	upload = FileField("Image upload", validators=[FileRequired(), FileAllowed(allowed_uploads, "Images Only!!")])