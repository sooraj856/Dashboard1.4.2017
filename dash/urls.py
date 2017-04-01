from django.conf.urls import url , include
from . import views


app_name = 'dash'
urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^todo/$', views.todo , name="todo"),
    url(r'^todo/taskedit/$', views.taskedit , name="taskedit"),
    url(r'^todo/statuschange/$', views.statuschange , name="statuschange"),
    url(r'^todo/statuscompleted/$', views.statuscompleted , name="statuscompleted"),
]
