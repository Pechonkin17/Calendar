from flask import render_template, Blueprint

index_bp = Blueprint('index', __name__, template_folder='../templates/index')

@index_bp.route('/')
def index():
    return render_template('index.html')