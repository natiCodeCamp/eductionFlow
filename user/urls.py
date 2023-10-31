from django.urls import path
from .views import getUser,SignUp,getProfile,UpdateProfile
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('get_user/',getUser),
    path('signup/',SignUp),
    path('getprofile/<int:id>',getProfile),
    path('update/<int:id>',UpdateProfile)
]