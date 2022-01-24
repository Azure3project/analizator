from app.ocr import *
from flask import flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from app.extracting import init_extracting, extract_products
from datetime import date
from app.models import Product
from app import app, db
from app.forms import AddProductForm

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
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.expire_date).paginate(page=page,
                                                                    per_page=10)
    return render_template('fridge.html', products=products)


@app.route('/fridge/add', methods=['POST', 'GET'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product = Product(product_name=form.product.data, expire_date=form.expire_date.data)
        db.session.add(product)
        db.session.commit()
        flash(f'The product was added to the fridge!')
        return redirect(url_for('my_fridge'))
    return render_template('add_product.html', form=form)


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
        message = ocr_function(filename)

        products, dates = extract_products(message)

        for i in range(len(products)):
            if dates[i] == date.today():
                product = Product(product_name=products[i])
            else:
                product = Product(product_name=products[i], expire_date=dates[i])
            db.session.add(product)
            db.session.commit()
        flash(f'The products were added to the fridge!')

        flash('Image successfully uploaded!')
        return render_template('receipt.html', filename=filename, message=message)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('app/static', filename='uploads/' + filename), code=301)
