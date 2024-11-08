from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Semester
from base import Session


semester_bp = Blueprint('semester', __name__, template_folder='../templates/semester')


@semester_bp.route('/semester/create', methods=['GET', 'POST'])
def create_semester():
    with Session() as session:

        if request.method == 'POST':
            name = request.form['name']
            year = request.form['year']

            new_semester = Semester(name=name, year=year)

            session.add(new_semester)
            session.commit()

            return redirect(url_for('semester.all_semesters'))

    return render_template('semester/create_semester.html')


@semester_bp.route('/semesters')
def all_semesters():
    with Session() as session:
        semesters = session.query(Semester).all()
    return render_template('semester/all_semesters.html', semesters=semesters)


@semester_bp.route('/semester/delete/<int:semester_id>', methods=["DELETE"])
def delete_semester(semester_id):
    with Session() as session:
        semester = session.query(Semester).get(semester_id)
        if semester:
            session.delete(semester)
            session.commit()
            return jsonify({"message": "Семестер видалено"}), 200

        return jsonify({"message": "Семестер не знайдено"}), 404