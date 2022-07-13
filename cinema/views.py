from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from rest_framework.permissions import IsAdminUser

from .models import Cinema, Genre, Category, Producer, Actor
from .forms import CinemaForm, CommentsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required 

# hash()

def myCinema(request):
    cinemas = Cinema.objects.all().order_by('name')
    genres = Genre.objects.all().order_by('name')

    if request.GET:
        if request.GET.get('genres'):
            cinemas = cinemas.filter(genres__name__exact=request.GET.get('genres'))

        if request.GET.get('release_date'):
            cinemas = cinemas.filter(release_date__exact=request.GET.get('release_date'))

    context = {
        'cinemas': cinemas,
        'genres': genres
    }
    return render(request, 'cinema/mycinema.html', context)


def movies(request):
    cinemas = Cinema.objects.all().order_by('name')
    cinemas = cinemas.filter(category__name__contains='movies')
    genres = Genre.objects.all().order_by('name')
    if request.GET:
        if request.GET.get('genres'):
            cinemas = cinemas.filter(genres__name__exact=request.GET.get('genres'))

        if request.GET.get('release_date'):
            cinemas = cinemas.filter(release_date__exact=request.GET.get('release_date'))

    context = {
        'cinemas': cinemas,
        'genres': genres
    }
    return render(request, 'cinema/movies.html', context)


def cartoons(request):
    cinemas = Cinema.objects.all().order_by('name')
    cinemas = cinemas.filter(category__name__contains='cartoons')
    genres = Genre.objects.all().order_by('name')
    if request.GET:
        if request.GET.get('genres'):
            cinemas = cinemas.filter(genres__name__exact=request.GET.get('genres'))

        if request.GET.get('release_date'):
            cinemas = cinemas.filter(release_date__exact=request.GET.get('release_date'))

    context = {
        'cinemas': cinemas,
        'genres': genres
    }

    return render(request, 'cinema/cartoons.html', context)


def serials(request):
    cinemas = Cinema.objects.all().order_by('name')
    cinemas = cinemas.filter(category__name__contains='serials')
    genres = Genre.objects.all().order_by('name')
    if request.GET:
        if request.GET.get('genres'):
            cinemas = cinemas.filter(genres__name__exact=request.GET.get('genres'))

        if request.GET.get('release_date'):
            cinemas = cinemas.filter(release_date__exact=request.GET.get('release_date'))

    context = {
        'cinemas': cinemas,
        'genres': genres
    }

    return render(request, 'cinema/serials.html', context)


class NewsDetailView(FormMixin, DetailView):
    model = Cinema
    template_name = 'cinema/details.html'
    context_object_name = 'cinema'
    form_class = CommentsForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
@staff_member_required
def update(request, pk):
    data = get_object_or_404(Cinema, pk=pk)
    form = CinemaForm(instance=data)

    if request.method == "POST":
        form = CinemaForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/cinema/')
    context = {
        "form": form
    }
    return render(request, 'cinema/create.html', context)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Cinema
    success_url = '/cinema/'
    template_name = 'cinema/delete.html'
    permission_required = 'cinema.delete_cinema'


@login_required
def create(request):
    error = ''
    content_genre = Genre.objects.all()
    content_category = Category.objects.all()
    content_producers = Producer.objects.all()
    content_actors = Actor.objects.all()
    if request.method == 'POST':
        form = CinemaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_cinema')
        else:
            error = 'The Form was incorrect!'

    form = CinemaForm()

    data = {
        'form': form,
        'error': error,
        'content_genre': content_genre,
        'content_category': content_category,
        'content_producers': content_producers,
        'content_actors': content_actors,
    }

    return render(request, 'cinema/create.html', data)
