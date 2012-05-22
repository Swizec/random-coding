# Create your views here.

from django.shortcuts import render_to_response

from talk_example.models import *

def home(request):
    return render_to_response('index.html', {
            'albums': Album.objects.all()
            })














def first(request):
    albums = []
    for album in Album.objects.all():
        albums.append({
                'title': album.title,
                'user': album.user_set.all()[0],
                'pics': album.pics.all()
                })

    return render_to_response('first.html', {
            'albums': albums
            })













def select(request):
    albums = []
    for album in Album.objects.all():
        albums.append({
                'title': album.title,
                'user': album.user_set.all()[0],
                'pics': album.pics.select_related().all()
                })

    return render_to_response('first.html', {
            'albums': albums
            })


















def prefetch(request):
    albums = []

    for album in Album.objects.all().prefetch_related('user_set'):
        albums.append({
                'title': album.title,
                'user': album.user_set.all()[0],
                'pics': album.pics.select_related().all().prefetch_related('comment_set',
                                                                           'comment_set__user')
                })

    return render_to_response('first.html', {
            'albums': albums
            })
