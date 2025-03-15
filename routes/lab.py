from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort

from db_queries.subject import get_subject
from db_queries.lab import create_lab_db, get_labs_in_subject_db, get_lab_db

lab_bp = Blueprint('labs', __name__)


@lab_bp.route('/labs/create/<int:subject_id>', methods=['POST'])
def create_lab(subject_id):
    subject = get_subject(subject_id)
    if subject is None:
        abort(404)

    name = request.form['name']
    description = request.form['description']
    max_points = int(request.form['max_points'])
    create_lab_db(name, description, max_points, subject_id)
    return "OK", 200


@lab_bp.route('/labs/<int:subject_id>', methods=['GET'])
def get_labs_in_subject(subject_id):
    subject = get_subject(subject_id)
    if subject is None:
        abort(404)
    else:
        labs = get_labs_in_subject_db(subject_id)
        return "OK", 200


@lab_bp.route('/labs/edit/<int:lab_id>', methods=['PATCH'])
def edit_lab(lab_id):
    lab = get_lab_db(lab_id)
    if lab is None:
        abort(404)

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

    return jsonify({"message": "Лабораторну успішно оновлено"}), 200


@lab_bp.route('/labs/delete/<int:lab_id>', methods=['DELETE'])
def delete_lab(lab_id):
    if request.method == 'DELETE':
        lab = get_lab_db(lab_id)
        if lab:
            return jsonify({"message": "Лабораторну видалено"}), 200
        return jsonify({"message": "Лабораторну не знайдено"}), 404