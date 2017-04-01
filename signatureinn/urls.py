from django.conf.urls import url , include
from . import views


app_name = 'signatureinn'
urlpatterns = [
    url(r'^homepage/$', views.homepage , name="homepage"),
    url(r'^homepage/dailyacs/$', views.dailyacs , name="dailyacs"),
    url(r'^homepage/dailyacs/dailyacsdata/$', views.dailyacsdata , name="dailyacsdata"),
    url(r'^homepage/dailyacs/calculatetotal/$', views.calculatetotal , name="calculatetotal"),
    url(r'^homepage/feedback/$', views.feedback , name="feedback"),
]
