from django.contrib import admin

from .models import Posts


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    # autocomplete_fields = ['title']
