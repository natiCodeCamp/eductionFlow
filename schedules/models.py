from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser,UserManager
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
from django.db import transaction
import os

def update_filename(instance, filename):
    print(instance.profile.name,filename)
    path = "profile/images/"
    format = f"{instance.user.id}/" + str(filename).replace(" ",'')
    return os.path.join(path, format)
# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(blank=True)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

class Subject(models.Model):
    subject =models.CharField(max_length=50,unique=True)
    def __str__(self):
        return f"{self.subject}"
class Grade(models.Model):
    grade=models.CharField(max_length=30,blank=True,unique=True)
    number=models.IntegerField()
    section=models.CharField(max_length=25,null=True,blank=True)
    subjects=models.ManyToManyField(Subject,blank=True)

    def save(self):
        self.grade = f"{self.number}{self.section}"
        return super().save()
    def __str__(self):
        return f"{self.grade}"

class Teacher(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    profile =models.ImageField(upload_to=update_filename,default='default/user.png',blank=True)
    subject=models.ForeignKey(Subject,models.SET_DEFAULT,to_field="subject",default="Maths",blank=True)

    def __str__(self):
        return self.user.username
    def save(self,*args,**kwargs):
        studentOrNot = Student.objects.filter(user=self.user).exists()
        if (studentOrNot):
            raise ValidationError
        else:
            super(Teacher, self).save(*args, **kwargs)




class Schedule(models.Model):
    teacher =models.ForeignKey(Teacher,on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade,models.CASCADE)
    subject=models.ForeignKey(Subject,models.CASCADE,blank=True)
    message = models.TextField()
    given_date = models.DateField(max_length=1000,default=date.today)
    submit_date=models.DateField(max_length=1000,null=True)
    catagories = models.CharField(choices=(('Homework','Homework'),('Worksheet','Worksheet'),('Assignment','Assignment'),('Study','Study')),max_length=100,blank=True,null=True)
    class Meta:
        ordering = ["-given_date"]
    def save(self,*args,**kwargs):
        self.subject = self.teacher.subject
        super(Schedule,self).save()
    def __str__(self):
        return f"{self.teacher}"
class Student(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to=update_filename,default='default/user.png',blank=True)
    grade =models.ForeignKey(Grade,on_delete=models.SET_DEFAULT,default=1,blank=True)
    bookmarks = models.ManyToManyField(Schedule,blank=True)

    def __str__(self):
        return self.user.username
    def save(self,*args,**kwargs):
        studentOrNot = Teacher.objects.filter(user=self.user).exists()
        if (studentOrNot):
            raise ValidationError
        else:
            super(Student, self).save(*args, **kwargs)


def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            try:
                with transaction.atomic():
                    Teacher.objects.create(user=instance)
            except Exception:
                pass
        else:
            try:
                with transaction.atomic():
                    Student.objects.create(user=instance)
            except Exception:
                pass


post_save.connect(create_profile, sender=MyUser, dispatch_uid="myUniqueSignal")
