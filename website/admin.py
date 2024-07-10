from django.contrib import admin
from .models import Category, Art, Artist

admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Art)

