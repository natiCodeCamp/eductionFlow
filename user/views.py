from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilazer import UserSerialzerStudent,UserSerialzerTeacher
import requests
from schedules.models import MyUser,Student,Grade,Teacher,Subject
from django.contrib.auth import authenticate
import urllib.request as urllib2
from django.core.files import File
# Create your views here.
@api_view(["post"])
def getUser(request):
    user_username =request.data.get("username")
    user_password =request.data.get("password")
    obj =authenticate(username=user_username,password=user_password)
    if obj is not None:
        if(obj.is_teacher):
            serialzer = UserSerialzerTeacher(obj)
        else:
            serialzer = UserSerialzerStudent(obj)
        return Response(serialzer.data)
    else:
        return Response({"error":"something went wrong"},status=406)
@api_view(['post'])
def GetUserGoogle(request):
    acsses_token=request.data.get("token")
    athunticated_user = requests.get(f"https://www.googleapis.com/oauth2/v3/userinfo?access_token={acsses_token}")
    user_data =athunticated_user.json()
    fiterer = MyUser.objects.filter(email=user_data.get('email'))
    if(fiterer):
        if(fiterer[0].is_teacher):
            serialzer = UserSerialzerTeacher(fiterer[0])
        else:
            serialzer = UserSerialzerStudent(fiterer[0])
        return Response({
            "SignUp":False,
            'data':serialzer.data
        })
    else:
        return Response({"SignUp":True,'data':user_data})

@api_view(["POST"])
def SignUp(request):
    firstname = request.data.get('firstname')
    lastname = request.data.get('lastname')
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    pic = request.data.get('pic')
    grade = request.data.get('grade')
    try:
        grade_obj = Grade.objects.get(id=int(grade))
        if(email == ""):
            user = MyUser.objects.create_user(username=username,last_name=lastname,first_name=firstname,password=password)
            profile = Student.objects.create(user=user)
        else:
            user = MyUser.objects.create_user(username=username,last_name=lastname,first_name=firstname,email=email,password=password)
            profile = Student.objects.create(user=user)
        if(pic):
            data =urllib2.urlopen(pic)
            file = File(data)
            profile.profile.save(user.username,file)
            file.close()
        if(grade_obj):
            print(grade,'testing')
            profile.grade = grade_obj
            profile.save()
        if(user.is_teacher):
            obj = UserSerialzerTeacher(user)
        else:
            obj =UserSerialzerStudent(user)
        return Response(obj.data)
    except Exception as e:
        print(e)
        return Response({"error":True},status=501)

@api_view(["GET"])
def getProfile(request,id):
    user = MyUser.objects.get(id=id)
    if(user.is_teacher):
        profile = UserSerialzerTeacher(user)
    else:
        profile =UserSerialzerStudent(user)
    return Response(profile.data)

@api_view(['POST'])
def UpdateProfile(request,id):
    user =MyUser.objects.get(id=id)
    username = request.data.get('username')
    firstname = request.data.get('firstname')
    lastname =request.data.get('lastname')
    email =request.data.get('email')
    profile=request.data.get('profilepic')
    subject=request.data.get('subject')
    grade = request.data.get('grade')
    user.username =username
    user.first_name =firstname
    user.last_name =lastname
    user.email =email
    user.save()
    if(user.is_teacher): 
        teacher =Teacher.objects.get(user=id)
        teacher_subject =Subject.objects.get(subject=subject)
        teacher.subject = teacher_subject       
        if(profile):
            teacher.profile = profile
        teacher.save()
        obj_ser = UserSerialzerTeacher(user)
    else:
        student =Student.objects.get(user=id)
        student_grade =Grade.objects.get(grade=grade)
        student.grade = student_grade
        if(profile):
            student.profile =profile
        student.save()
        obj_ser = UserSerialzerStudent(user)
    return Response(obj_ser.data,status=201)
           
        


