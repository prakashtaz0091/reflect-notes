from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("post-a-question/",views.postAQuestion,name='postAQuestion'),
    path("answer/<int:pk>",views.answer,name='answer'),
]