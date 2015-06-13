# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, Tag
from forms import PostForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
