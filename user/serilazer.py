from rest_framework.serializers import ModelSerializer
from schedules.models import Teacher,Student
from schedules.serailzer import GradeSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
class TeacherSerializer(ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','subject','profile']

class StudentSerializer(ModelSerializer):
    grade = GradeSerializer()
    class Meta:
        model=Student
        fields=['grade','profile']
        depth = 2
class UserSerialzerStudent(ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = User
        fields = ["id","username","email","first_name",'last_name','student' , "is_teacher"]
        depth = 2
class UserSerialzerTeacher(ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = User
        fields = ["id","username","email","first_name",'last_name','teacher',"is_teacher"]
        depth = 2