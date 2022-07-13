from django.urls import path
from . import views

urlpatterns = [
    path('', views.myCinema, name='home_cinema'),
    path('create', views.create, name='create'),
    path('movies', views.movies, name='movies'),
    path('cartoons', views.cartoons, name='cartoons'),
    path('serials', views.serials, name='serials'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete')
]
