from django.contrib import admin
from .models import NewPost


@admin.register(NewPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title', 'content')
    list_filter = ('pub_date', 'author')
