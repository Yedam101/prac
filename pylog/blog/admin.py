from django.contrib import admin
from .models import Post, Comment

@admin.register
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register
class CommentAdmin(admin.ModelAdmin):
    pass