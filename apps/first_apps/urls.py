from django.conf.urls import url
from . import views

           
urlpatterns = [
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^login/$', views.login),
	url(r'^register/$', views.create),
	url(r'^$', views.index)
] 







