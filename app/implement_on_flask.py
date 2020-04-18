import os
from flask import Flask, flash, request, redirect, url_for , render_template , send_from_directory
from werkzeug.utils import secure_filename
from dream_image import processing

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/create_dream', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file'))
    return render_template("upload.html")

@app.route('/templates/')
def uploaded_file():
    Path = os.path.join(app.config['UPLOAD_FOLDER'],)
    #processing(str(Path))
    return "your image will be processed"
    #return redirect(url_for('upload_file'))

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
