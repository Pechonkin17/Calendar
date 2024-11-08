from flask import render_template, Blueprint
from models import Semester
from base import Session


index_bp = Blueprint('index', __name__, template_folder='../templates/index')

@index_bp.route('/')
def index():
    with Session() as session:
        semesters = session.query(Semester).all()

    return render_template('index.html', semesters=semesters)