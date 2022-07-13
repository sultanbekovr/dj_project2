from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from django.urls import reverse


class Category(models.Model):
    """ Categories """
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    """ Actors """
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


class Producer(models.Model):
    """ Producers """
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='producers/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Genre(models.Model):
    """ Genres """
    name = models.CharField('Name', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Cinema(models.Model):
    """ Cinemas """
    img = models.ImageField('Image of cinema', upload_to='images/')
    name = models.CharField('Name of cinema', max_length=300)
    release_date = models.PositiveSmallIntegerField('Release Date', default=2022)
    country = models.CharField('Country', max_length=300)
    description = models.TextField('Description')
    directors = models.ManyToManyField(Producer, verbose_name='producer', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='actors', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='genres')
    budget = models.PositiveSmallIntegerField('Budget')
    fees_usa = models.PositiveSmallIntegerField('Fees in USA')
    fees_world = models.PositiveSmallIntegerField('Fees in the World')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    allowable_age = models.IntegerField('Allowable age')
    rating = models.CharField('Rating in Kinopoisk', max_length=300)
    rating_imdb = models.CharField('Rating in IMDB', max_length=300)
    time_duration = models.CharField('Time Duration', max_length=300)

    def get_absolute_url(self):
        return f'/cinema/{self.pk}/update'
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Cinema'
        verbose_name_plural = 'Cinemas'
        ordering = ['name', 'rating']


class Comments(models.Model):
    """ Comments """
    title = models.CharField(max_length=250, verbose_name='Title of comments')
    name = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Name of cinema', blank=True, null=True,
                             related_name='comments_cinemas')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author of comments', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text of comments')
    status = models.BooleanField(verbose_name='Cinema visibility', default=True)

    @property
    def short_text(self):
        return truncatechars(self.text, 10)

    def __str__(self):
        return f"{str(self.author)} - {str(self.name)}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class MyCinemaCatalog(models.Model):
    name = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Select a cinema', related_name='mycinemas')

