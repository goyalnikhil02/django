from django.views import generic
from .models import Album
from  django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = "all"




    def get_queryset(self):
        return  Album.objects.all()



class DetailsView(generic.DetailView):
    model=Album
    template_name = 'music/details.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class Albumdelete(DeleteView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


