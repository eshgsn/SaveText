from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'user-data', views.UserDataViewSet)



urlpatterns = [
    path("",views.home),
    path("login",views.login_user),
    path("SignUp",views.save_user),
    path("register",views.signup),
    path("textarea",views.textarea),
    path('api-auth', include('rest_framework.urls')),
    path('', include(router.urls)),
    # path("save")

]