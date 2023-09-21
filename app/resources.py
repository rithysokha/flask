from flask_restx import Namespace, Resource
from .api_models import course_model, student_model, course_input_model
from .models import Course, Student, db
ns = Namespace('api')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@ns.route('/course')
class CourseApi(Resource):
    @ns.marshal_list_with(course_model)
    @ns.marshal_with(course_model)
    def get(self):
        return Course.query.all()
    @ns.expect(course_input_model)
    def post(self):
        course = Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course

@ns.route('/student')
class StudentApi(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()