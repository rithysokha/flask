from .extensions import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    
    course = db.relationship("Course", back_populates="instrutor")

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    student = db.relationship("Student", back_populates="course")
    instructor = db.relationship("User", back_populates="course")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    course = db.relationship("Course", back_populates="student")
