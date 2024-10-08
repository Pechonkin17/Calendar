from flask import Blueprint, render_template, request, redirect, url_for
from models import Lab, Subject
from base import Session

lab_bp = Blueprint('labs', __name__, template_folder='../templates/labs')

@lab_bp.route('/labs/create/<int:subject_id>', methods=['GET', 'POST'])
def create_lab(subject_id):
    with Session() as session:
        subject = session.query(Subject).get(subject_id)

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            max_points = int(request.form['max_points'])

            new_lab = Lab(name=name, description=description, max_points=max_points, subject_id=subject_id)

            session.add(new_lab)
            session.commit()

            return redirect(url_for('labs.view_labs', subject_id=subject_id))

    return render_template('labs/create.html', subject=subject)

@lab_bp.route('/labs/<int:subject_id>')
def view_labs(subject_id):
    session = Session()
    subject = session.query(Subject).get(subject_id)
    labs = session.query(Lab).filter_by(subject_id=subject_id).all()
    return render_template('labs/list.html', labs=labs, subject=subject)

