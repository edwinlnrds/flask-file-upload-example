import os

from flask import Flask, flash, request
from flask.templating import render_template
from werkzeug.utils import redirect, secure_filename

from forms import UploadForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "hereby, secret key"
app.config["UPLOAD_FOLDER"] = "./static/uploads"
app.config["MAX_CONTENT_LENGTH"] = (
    # Maksimal ukuran upload file 10 Megabyte
    10 * 1000 * 1000
)


@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    if request.method == "POST" and form.validate():
        file = request.files["file"]
        try:
            if file.filename == '':
                flash('File belum dipilih', 'warning')

            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                flash("Upload file berhasil", "success")
        except Exception as e:
            flash(f'{e}', 'danger')

        redirect(request.referrer)

    # Mengambil nama file yang sudah di upload
    filenames = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("index.html", form=form, filenames=filenames)
