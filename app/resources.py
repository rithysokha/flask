from flask_restx import Namespace, Resource
from .api_models import course_model, student_model
from .models import Course, Student
ns = Namespace('api')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@ns.route('/course')
class CourseApi(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
@ns.route('/student')
class StudentApi(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()