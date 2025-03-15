from base import db_session
from models import Semester


@db_session
def get_semester_db(session, semester_id):
    return session.query(Semester).get(semester_id)


@db_session
def get_semesters_db(session):
    semesters = session.query(Semester).all()
    return semesters


@db_session
def create_semester_db(session, name, year):
    semester = Semester(name=name, year=year)
    session.add(semester)
    session.commit()


@db_session
def delete_semester_db(session, semester_id):
    semester = session.query(Semester).filter(Semester.id == semester_id).first()
    if semester:
        session.delete(semester)
        session.commit()
        return True
    return False