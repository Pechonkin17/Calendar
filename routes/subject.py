from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort

from db_queries.semester import get_semester_db
from db_queries.subject import create_subject_db, get_subjects_in_semester_db, get_subject

subject_bp = Blueprint('subjects', __name__)


@subject_bp.route('/subjects/create/<int:semester_id>', methods=['POST'])
def create_subject(semester_id):
    semester = get_semester_db(semester_id)
    if semester is None:
        abort(404)

    title = request.form['title']
    description = request.form['description']
    create_subject_db(title, description, semester_id)
    return "OK", 200


@subject_bp.route('/subjects/<int:semester_id>', methods=['GET'])
def get_subjects(semester_id):
    semester = get_semester_db(semester_id)
    subjects = get_subjects_in_semester_db(semester_id)
    return "OK", 200


@subject_bp.route('/subjects/edit/<int:subject_id>', methods=["PATCH"])
def edit_subject(subject_id):
    subject = get_subject(subject_id)
    if subject is None:
        abort(404)

    title = request.form['title']
    description = request.form['description']

    if title:
        subject.title = title
    if description:
        subject.description = description
    return jsonify({"message": "Предмет успішно оновлено"}), 200


@subject_bp.route('/subjects/delete/<int:subject_id>', methods=["DELETE"])
def delete_subject(subject_id):
    subject = get_subject(subject_id)
    if subject:
        return jsonify({"message": "Предмет видалено"}), 200
    else:
        return jsonify({"message": "Предмет не знайдено"}), 404