from rest_framework.serializers import ModelSerializer
from .models import Schedule,Grade,Subject,Teacher,MyUser

class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["id"]
class UserSerializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields = ['id','username',"first_name","last_name"]
class TeacherSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=Teacher
        fields = ['id','user','subject']
class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject']
class GradeSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Grade
        fields = ["id","grade",'number','section',"subjects"]
class GradeSerializer2(ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Grade
        fields = ['subjects']
class GradeOnlySerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade']

class TeacherSerializerForSchedule(ModelSerializer):
    class Meta:
        model=Teacher
        fields = ['id']
class ScheduleSerialzer(ModelSerializer):
    subject =  SubjectSerializer()
    teacher =   TeacherSerializerForSchedule()
    class Meta:
        model =Schedule
        fields = '__all__'
        depth = 1