from django.urls import path
from .views import getUser,GetUserGoogle,SignUp,getProfile,UpdateProfile
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('get_user/',getUser),
    path('get_user_google/',GetUserGoogle),
    path('signup/',SignUp),
    path('getprofile/<int:id>',getProfile),
    path('update/<int:id>',UpdateProfile)
]