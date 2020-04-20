import os
from flask import Flask, flash, request, redirect, url_for , render_template , send_from_directory
from werkzeug.utils import secure_filename
from dream_image import processing

UPLOAD_FOLDER = 'static/assets/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
counter = 0

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def name_a_file(filename):
    filename = filename.split(".")
    global counter
    filename = str(counter) + "." + str(filename[1])
    counter+=1
    return filename

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
            filename = name_a_file(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file'  , filename=filename))
    return render_template("upload.html")

@app.route('/templates/<filename>')
def uploaded_file(filename):
    Path = os.path.join(app.config['UPLOAD_FOLDER'] , filename)
    processing(str(Path))
    Path = Path.split(".")
    Path = str(Path[0]) + "_out." + str(Path[1])
    return render_template("show_uploaded_file.html" , path=Path)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
