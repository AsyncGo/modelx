from flask import Blueprint

execute = Blueprint('execute', __name__, url_prefix='/execute')


@execute.route('/model')
def model():
	return 'runing...'


