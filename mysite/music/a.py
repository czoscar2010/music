#########tutorial 14

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album 

def index(request):
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	context = {
		'all_albums' : all_albums,
	}
	return HttpResponse(template.render(context,request))
	
def detail(request,album_id):
	return HttpResponse("<h2>Details for Album id: "+ str(album_id) +"</h2>")
	
	
	##############t 20
	def index(request):
	all_albums = Album.objects.all()
	##template = loader.get_template('music/index.html')
	context = {'all_albums' : all_albums}
	return render(request, 'music/index.html' , context)
	
def detail(request,album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album doese not exist")
	return render(request, 'music/detail.html' , {'album' : album})
	
###########23
<ul>
	{% for song in album.song_set.all %}
	<li>{{ song.song_title }} - {{ song.file_type }}</li>
	{% endfor %}
</ul>