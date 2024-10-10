from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.subject import Subject
from base import Session


subject_bp = Blueprint('subjects', __name__, template_folder='../templates/subjects')


@subject_bp.route('/subjects/create', methods=['GET', 'POST'])
def create_subject():
    with Session() as session:

        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']

            new_subject = Subject(title=title, description=description)

            session.add(new_subject)
            session.commit()

            return redirect(url_for('subjects.view_subjects'))

    return render_template('subjects/create_subject.html')


@subject_bp.route('/subjects')
def view_subjects():
    session = Session()
    subjects = session.query(Subject).all()
    return render_template('subjects/view_subjects.html', subjects=subjects)


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