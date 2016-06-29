
from django.conf.urls import url
from online import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^login/$', views.login, name='login'),
	url(r'^regist/$', views.regist, name='regist'),
	url(r'^index/$', views.index, name='index'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^newitem/$', views.newitem, name='newitem'),
	url(r'^itemlist/$', views.itemlist, name='itemlist'),
	url(r'^photolist/$', views.photolist, name='photolist'),
	url(r'^download/$', views.download, name='download'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^photo/(?P<path>.*)', views.photolist, {'document_root': 'E:\django\mysite5\photo'}),



]

"""
from django.conf.urls import patterns, url
from online import views


urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
)
"""
