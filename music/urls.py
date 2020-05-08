from django.conf.urls import url
from . import views

urlpatterns=[
    #/music/
    url(r'^$',views.index,name='index'),

    #/music/71/
    #The coming variable is saved inside the variable album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]