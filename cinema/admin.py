from django.contrib import admin
from .models import Cinema, Genre, Actor, Producer, Category, Comments

admin.site.register(Cinema)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Producer)
admin.site.register(Category)
admin.site.register(Comments)
