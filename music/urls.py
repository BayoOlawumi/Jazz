from django.conf.urls import url
from . import views


app_name='music'
urlpatterns=[
    #/music/
    url(r'^$',views.index,name='index'),
    #/music/71/
    #/music/<album_id>/
    #The coming variable is saved inside the variable album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #/music/71/favourite
    #/music/<album_id>/<favourite>
    #The coming variable is saved inside the variable album_id
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]