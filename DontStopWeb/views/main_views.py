from flask import Blueprint, render_template, url_for, current_app
from werkzeug.utils import redirect
from flask import request


bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'

@bp.route('/', methods= ['POST','GET'])
def index():
    return render_template('index.html')

@bp.route('/inquire', methods=['GET'])
def inquire():
    return render_template('inquire.html')

@bp.route('/inquire_food', methods=['GET'])
def inquire_food():
    return render_template('inquire_food.html')

@bp.route('/inquire_cafe', methods=['GET'])
def inquire_cafe():
    return render_template('inquire_cafe.html')

@bp.route('/notice', methods=['GET'])
def notice():
    return render_template('notice.html')


@bp.route('/inquire_process', methods=['post'])
def inquire_process():
    if request.method == 'POST':
        item = request.form.getlist('checkOptions')
        name = request.form['name']
        business = request.form['radioOptions']
        duty = request.form['list']
        email = request.form['email']
        phone = request.form['phone']
        comment = request.form['comment']

        cursor = db.cursor()
        query = "INSERT INTO Simple_Counseling(name, phone, duty, email, comment, item, business) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,phone,duty,email,comment,item,business))

        db.commit()
        cursor.close()
    return render_template('index.html')

@bp.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['comments']

        cursor = db.cursor()
        query = "INSERT INTO Counseling(name, email, comment) VALUES (%s, %s,%s)"
        cursor.execute(query,(name,email,message))

        db.commit()
        cursor.close()
        return render_template('index.html')
    else:
        return render_template('index.html')