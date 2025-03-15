from base import db_session
from models import Lab, Subject


@db_session
def create_lab_db(session, name, description, max_points, subject_id):
    lab = Lab(name=name, description=description, max_points=max_points, subject_id=subject_id)
    session.add(lab)
    session.commit()


@db_session
def get_labs_in_subject_db(session, subject_id):
    return session.query(Lab).filter_by(subject_id=subject_id).all()


@db_session
def get_lab_db(session, lab_id):
    return session.query(Lab).filter_by(id=lab_id).first()


@db_session
def delete_lab_db(session, lab):
    session.delete(lab)
    session.commit()