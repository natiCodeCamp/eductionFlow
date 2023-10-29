from django.urls import path
from .views import (search,getAllGrades,getGrade,
                    bookmark,getBookmarks,removeBookmark,
                    getAllBookmarks,getAllSubjects,getRelatedSubjectsWithGrade,
                    getBothAllGradesAndSubjects,getSchedulesByCreater,createSchedule,updateSchedule
                    ,deleteSchedule)

urlpatterns =[
    path('',search),
    path('getGrades/',getAllGrades),
    path('get-all-subjects/',getAllSubjects),
    path('get-subjects/',getGrade),
    path('bookmark/',bookmark),
    path('getbookmarks/',getBookmarks),
    path('removebookmark/',removeBookmark),
    path('getallbookmarks/',getAllBookmarks),
    path('get-grades/',getRelatedSubjectsWithGrade),
    path('get-both-grades-and-subjects/',getBothAllGradesAndSubjects),
    path('my-schedules/<int:id>',getSchedulesByCreater),
    path('create-schedule/',createSchedule),
    path('update-schedule/<int:id>',updateSchedule),
    path('delete-schedule/<int:id>',deleteSchedule),

]