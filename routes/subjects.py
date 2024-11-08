from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Subject, Semester
from base import Session


subject_bp = Blueprint('subjects', __name__, template_folder='../templates/subjects')


@subject_bp.route('/subjects/create/<int:semester_id>', methods=['GET', 'POST'])
def create_subject(semester_id):
    with Session() as session:
        semester = session.query(Semester).get(semester_id)

        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']

            new_subject = Subject(title=title, description=description, semester_id=semester_id)

            session.add(new_subject)
            session.commit()

            return redirect(url_for('subjects.view_subjects', semester_id=semester_id))

    return render_template('subjects/create_subject.html', semester=semester)


@subject_bp.route('/subjects/<int:semester_id>')
def view_subjects(semester_id):
    with Session() as session:
        semester = session.query(Semester).get(semester_id)
        subjects = session.query(Subject).filter_by(semester_id=semester_id).all()
    return render_template('subjects/view_subjects.html', subjects=subjects, semester=semester)


@subject_bp.route('/subjects/edit/<int:subject_id>', methods=["GET", "PATCH"])
def edit_subject(subject_id):
    with Session() as session:
        subject = session.query(Subject).get(subject_id)

        if request.method == 'PATCH':
            title = request.form['title']
            description = request.form['description']

            if title:
                subject.title = title
            if description:
                subject.description = description

            session.commit()
            return jsonify({"message": "Предмет успішно оновлено"}), 200

        return render_template('subjects/edit_subject.html', subject=subject)


@subject_bp.route('/subjects/delete/<int:subject_id>', methods=["DELETE"])
def delete_subject(subject_id):
    with Session() as session:
        subject = session.query(Subject).get(subject_id)
        if subject:
            session.delete(subject)
            session.commit()
            return jsonify({"message": "Предмет видалено"}), 200

        return jsonify({"message": "Предмет не знайдено"}), 404