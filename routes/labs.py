from flask import Blueprint, render_template, request, redirect, url_for, jsonify
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

    return render_template('labs/create_lab.html', subject=subject)


@lab_bp.route('/labs/<int:subject_id>')
def view_labs(subject_id):
    with Session() as session:
        subject = session.query(Subject).get(subject_id)
        labs = session.query(Lab).filter_by(subject_id=subject_id).all()
    return render_template('labs/view_labs.html', labs=labs, subject=subject)


@lab_bp.route('/labs/edit/<int:lab_id>', methods=['GET', 'PATCH'])
def edit_lab(lab_id):
    with Session() as session:
        lab = session.query(Lab).get(lab_id)

        if request.method == 'PATCH':
            name = request.form['name']
            description = request.form['description']
            max_points = int(request.form['max_points'])
            is_submitted = request.form.get('is_submitted') == 'on'
            received_points = request.form.get('received_points')

            if name:
                lab.name = name
            if description:
                lab.description = description
            if max_points:
                lab.max_points = max_points
            lab.is_submitted = is_submitted
            if received_points is not None:
                lab.received_points = int(received_points)

            session.commit()
            return jsonify({"message": "Лабораторну успішно оновлено"}), 200

        return render_template('labs/edit_lab.html', lab=lab)


@lab_bp.route('/labs/delete/<int:lab_id>', methods=['DELETE'])
def delete_lab(lab_id):
    with Session() as session:
        lab = session.query(Lab).get(lab_id)
        if lab:
            session.delete(lab)
            session.commit()
            return jsonify({"message": "Лабораторну видалено"}), 200

        return jsonify({"message": "Лабораторну не знайдено"}), 404