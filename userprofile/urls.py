from django.urls import path

from userprofile import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey', views.survey, name='survey'),
    #path('register', views.register, name = 'register'),
    path('intro', views.intro, name = 'intro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name ='logout'),
    path('match', views.match, name='match')

]