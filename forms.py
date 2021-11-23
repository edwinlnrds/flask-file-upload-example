from flask.app import Flask
from flask_wtf import Form
from wtforms import FileField, SubmitField


class UploadForm(Form):
    file = FileField('Pilih File yang ingin di upload')
    upload = SubmitField('Upload')
