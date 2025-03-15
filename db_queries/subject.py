from base import db_session
from models import Subject

@db_session
def create_subject_db(session, title, description, semester_id):
    subject = Subject(title=title, description=description, semester_id=semester_id)
    session.add(subject)
    session.commit()


@db_session
def get_subjects_in_semester_db(session, semester_id):
    return session.query(Subject).filter(Subject.semester_id==semester_id).all()


@db_session
def get_subject(session, subject_id):
    return session.query(Subject).filter(id==subject_id).first()


@db_session
def update_subject_db(session, subject):
    session.add(subject)
    session.commit()


@db_session
def delete_subject_db(session, subject):
    session.delete(subject)
    session.commit()