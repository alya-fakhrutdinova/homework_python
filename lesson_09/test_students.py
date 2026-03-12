from models import Student



def test_create_student(db_session):
    student = Student(email="test_student@example.com")
    db_session.add(student)
    db_session.commit()

    saved_student = db_session.query(Student).filter_by(
        email="test_student@example.com"
    ).one()
    assert saved_student.email == "test_student@example.com"
    assert saved_student.deleted_at is None

    db_session.delete(saved_student)
    db_session.commit()



def test_update_student_email(db_session):
    student = Student(email="old_email@example.com")
    db_session.add(student)
    db_session.commit()

    student.email = "new_email@example.com"
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(id=student.id).one()
    assert updated_student.email == "new_email@example.com"

    db_session.delete(updated_student)
    db_session.commit()



def test_soft_delete_student(db_session):
    student = Student(email="delete_me@example.com")
    db_session.add(student)
    db_session.commit()

    student.soft_delete()
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(id=student.id).one()
    assert deleted_student.deleted_at is not None

    db_session.delete(deleted_student)
    db_session.commit()
