from ocr import *
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from extracting import init_extracting

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
init_extracting()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/receipt')
def new_receipt():
    return render_template('receipt.html')


@app.route('/fridge', methods=['POST', 'GET'])
def my_fridge():
    return render_template('fridge.html')


@app.route('/receipt', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part!')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading!')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      #  message = ocr_function(filename)
        flash('Image successfully uploaded!')
        return render_template('receipt.html', filename=filename, message=message)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/ocr<filename>')
def ocr(filename):
  #  message = ocr_function()
    return render_template("receipt.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
