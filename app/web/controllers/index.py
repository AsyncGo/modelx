from flask import Blueprint, render_template

index = Blueprint('index', __name__, url_prefix='/index', template_folder='../views/template/index', static_folder='../views/static')


@index.route('/')
def home():
	return render_template('home.html')


@index.route('/heart')
def heart():
	return 'OK'

