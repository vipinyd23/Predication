from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from .import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('predict/',views.predict,name='predict'),
    path("predict/result",views.result),
    path("cancer/",views.cancer,name='cancer'),
    path("cancer/res2",views.res1),
    path("heart/",views.heart,name='heart'),  
    path("heart/res1",views.res1),  
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),

]
