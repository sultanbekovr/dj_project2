from django.shortcuts import render

from cinema.models import *


def index(request):
    cinemas = Cinema.objects.all().order_by('name')

    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Cinema.objects.filter(name__contains=searched)
        return render(request, 'main/index.html', {'searched': searched, 'venues': venues})

    if request.GET:
        if request.GET.get('genres'):
            cinemas = cinemas.filter(genres__name__exact=request.GET.get('genres'))

        if request.GET.get('release_date'):
            cinemas = cinemas.filter(release_date__exact=request.GET.get('release_date'))

        if request.GET.get('actors'):
            cinemas = cinemas.filter(actors__name__exact=request.GET.get('actors'))

        if request.GET.get('category'):
            cinemas = cinemas.filter(category__name__exact=request.GET.get('category'))

    genres = Genre.objects.all().order_by('name')
    actors = Actor.objects.all().order_by('name')
    category = Category.objects.all()
    movies = cinemas.filter(category__name__exact='Movies')
    top_movies = movies.order_by('-rating')[:5]
    cartoons = cinemas.filter(category__name__exact='Cartoons')
    top_cartoons = cartoons.order_by('-rating')[:5]
    serials = cinemas.filter(category__name__exact='Serials')
    top_serials = serials.order_by('-rating')[:5]
    last_comments = Comments.objects.all().order_by('-create_date')[:5]

    context = {
        'cinemas': cinemas,
        'genres': genres,
        'actors': actors,
        'category': category,
        'top_movies': top_movies,
        'top_cartoons': top_cartoons,
        'top_serials': top_serials,
        'last_comments': last_comments
    }

    return render(request, 'main/index.html', context)
