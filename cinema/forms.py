from .models import Cinema, Comments
from django.forms import ModelForm, TextInput, DateInput, Textarea, Select


class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = ['img', 'name', 'release_date', 'country', 'genres', 'category', 'description', 'directors', 'actors',
                  'fees_usa', 'fees_world', 'budget', 'allowable_age',
                  'rating', 'rating_imdb', 'time_duration']

        labels = {
            'img': '',
            'name': '',
            'release_date': '',
            'country': '',
            'genres': '',
            'category': '',
            'description': '',
            'directors': '',
            'actors': '',
            'budget': '',
            'fees_usa': '',
            'fees_world': '',
            'allowable_age': '',
            'rating': '',
            'rating_imdb': '',
            'time_duration': '',
        }

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cinema name'
            }),
            "release_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Release date'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cinema country'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Cinema category'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Cinema description'
            }),
            "fees_usa": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fees in USA'
            }),
            "fees_world": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fees in the World'
            }),
            "budget": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cinema budget'
            }),
            "allowable_age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Allowable Age'
            }),
            "rating": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rating in kinopoisk'
            }),
            "rating_imdb": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rating in IMDB'
            }),
            "time_duration": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Time Duration'
            }),
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Comment's title"
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Comment's text"
            }),
        }
