from django.conf.urls import url

from todo.views import todoadd,todoedit,tododelete,todolist,about

urlpatterns=[
    url(r'^$',todolist,name='todolist'),
     url(r'^about/$',about,name='about'),
    url(r'^add/$',todoadd,name='todoadd'),
    url(r'^edit/(?P<pk>\d+)$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)$',tododelete,name='tododelete'),
    ]
