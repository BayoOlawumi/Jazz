from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Album
from .models import Song


# Create your views here.
def index(request):
    # obtains all the albums
    all_albums = Album.objects.all()
    # The template variable is reference to the file that will be seen
    # we never needed to do root directory to the template considered as this is being done automatically
    # Ensure you have your template in your app named ##templates
    #template = loader.get_template('music/index.html')
    # The context gives the data that is to be passed to the template for it to work
    context = {'all_albums': all_albums}
    #html = ' '
    # loops through the albums and create url for them
    # for album in all_albums:
    # url='/music/' + str(album.id) + '/'
    # html+='<a href="'+url+'">'+album.pub_name+'</a></br>'
    #we can use render in place of HttpResponse but in that case one has to use template.loader
    return render(request,'music/index.html',context)



def detail(request, album_id):
    try:
        # Get single element that meets up given
        album = Album.objects.get(id=album_id)
        # get songs that meets up the condition given
        albumSongs = Song.objects.filter(album=album)
        # map this function to a template, in this case albumSongs.html
        # template=loader.get_template('music/albumSongs.html')
        context = {'albumSongs': albumSongs}

    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/albumSongs.html', context)

