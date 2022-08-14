from django.contrib import admin
from django.urls import path
from trains import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),   # login.html page or starting page
    path('index', views.index),  # login.html page or starting page
    path('add',views.addTrain),
    path('fetch',views.fetch),
    path('update',views.update),
    path('delete',views.delete),
    path('mod',views.modify),
    path('contactus',views.contactus),
    path('login', views.login),
    path('register', views.register),
    path('home',views.home),
    path('logout', views.logout),
    path('mail',views.mail),
    path('enquire', views.enquire),
]
