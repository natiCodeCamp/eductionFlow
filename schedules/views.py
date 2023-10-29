from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailzer import ScheduleSerialzer,GradeSerializer,BookmarkSerializer,SubjectSerializer,GradeOnlySerializer
from  .models import Schedule,Grade,Subject,Student,MyUser
from .tools import Switch
import json
# Create your views here.
@api_view(["GET"])
def search(request):
    if (request.GET == {} ):
        seriliazer =ScheduleSerialzer(Schedule.objects.all(),many=True)
        return Response(seriliazer.data)
    else:
        grade = request.GET.get('grade')
        subject=request.GET.get("subject")
        date_given = request.GET.get("given_date")
        date_submitted = request.GET.get("submit_date")
        catagory = request.GET.get('catagory')
        data = Switch(grade,subject,date_given,date_submitted,catagory)
        seriliazer =ScheduleSerialzer(data,many=True)
        return Response({ "data":seriliazer.data })

@api_view(['GET'])
def getAllGrades(request):
    if(request.GET.get('subject')):
        subject =Subject.objects.get(subject=request.GET.get('subject')) 
        subject_obj =Grade.objects.filter(subjects=subject).exclude(grade="0A")
    else:
        subject_obj =Grade.objects.all().exclude(grade="0A")
    serilazer =GradeSerializer(subject_obj,many=True)
    return Response(serilazer.data)
@api_view(['GET'])
def getAllSubjects(request):
    serilazer =SubjectSerializer(Subject.objects.all(),many=True)
    return Response(serilazer.data)
@api_view(['GET'])
def getBothAllGradesAndSubjects(request):
    grades = GradeOnlySerializer(Grade.objects.all().exclude(grade="0A"),many=True)
    subject =SubjectSerializer(Subject.objects.all(),many=True)
    return Response({"grades":grades.data,"subjects":subject.data})
@api_view(['GET'])
def getGrade(request):
    grade = Grade.objects.get(grade=request.GET.get('grade'))
    serializer = GradeSerializer(grade)
    return Response(serializer.data)
@api_view(['GET'])
def getRelatedSubjectsWithGrade(request):
    subject =Subject.objects.get(subject=request.GET.get('subject'))
    grade = Grade.objects.filter(subjects=subject)
    serializer = GradeSerializer(grade,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getSchedulesByCreater(request,id):
    user =MyUser.objects.get(id=id)
    if(user.is_teacher):
        teacher = user.teacher
        schedules = Schedule.objects.filter(teacher=teacher)
        serialzer = ScheduleSerialzer(schedules,many=True)
        return Response(serialzer.data)
@api_view(['POST'])
def bookmark(request):
    try:
        schedule = request.data.get('schedule')
        id =request.data.get('id')
        stu =Student.objects.get(user=MyUser.objects.get(id=id))
        stu.bookmarks.add(schedule)
        return Response({"data":"workes"})
    except Exception as e:
        return Response({"error":e},status=403)
@api_view(['POST'])
def removeBookmark(request):
    try:
        schedule = request.data.get('schedule')
        id =request.data.get('id')
        stu =Student.objects.get(user=id)
        stu.bookmarks.remove(schedule)
        return Response({"data":"workes"})
    except Exception as e:
        return Response({"error":e},status=403)
    
@api_view(['GET'])
def getBookmarks(request):
    try:
        user =Student.objects.get(user=request.GET.get('id'))
        print(user)
        bookmarks =BookmarkSerializer(user.bookmarks.all().order_by('-given_date'),many=True) 
        return Response(bookmarks.data)
    except Exception as e:
        print(e)
        return Response(status=403)
@api_view(['GET'])    
def getAllBookmarks(request):
    try:
        user =Student.objects.get(user=request.GET.get('id'))
        print(user)
        bookmarks =ScheduleSerialzer(user.bookmarks.all().order_by('-given_date'),many=True) 
        return Response(bookmarks.data)
    except Exception as e:
        print(e)
        return Response(status=403)
    
@api_view(['POST'])
def createSchedule(request):
    user =int(request.data.get('user'))
    subject =Subject.objects.get(subject=request.data.get('subject'))
    grade =int(request.data.get('grade'))
    catagory =request.data.get('catagory')
    message = request.data.get('message')
    date =request.data.get('date')
    try:
        schedule = Schedule.objects.create(teacher_id=user,message=message,catagories=catagory,submit_date=date,grade_id=grade,subject=subject)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)
    
@api_view(['POST'])
def updateSchedule(request,id):
    grade =int(request.data.get('grade'))
    catagory =request.data.get('catagory')
    message = request.data.get('message')
    date =request.data.get('date')
    try:
        Schedule.objects.filter(id=id).update(grade_id=grade,catagories=catagory,message=message,submit_date=date)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)
    
@api_view(['DELETE'])
def deleteSchedule(request,id):
    obj = Schedule.objects.get(id=id)
    if(obj):
        obj.delete()
        return Response(status=200)