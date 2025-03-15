from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from db_queries.semester import get_semesters_db, create_semester_db, delete_semester_db


semester_bp = Blueprint('semester', __name__)


@semester_bp.route('/', methods=['GET'])
def get_semesters():
    semesters = get_semesters_db
    return "OK", 200


@semester_bp.route('/semesters/new', methods=['POST'])
def create_semester():
    name = request.form['name']
    year = request.form['year']
    create_semester_db(name, year)
    return "OK", 200


@semester_bp.route('/semester/delete/<int:semester_id>', methods=["DELETE"])
def delete_semester(semester_id):
    is_deleted = delete_semester_db(semester_id)
    if is_deleted:
        return jsonify({"message": "Семестер видалено"}), 200
    else:
        return jsonify({"message": "Семестер не знайдено"}), 404