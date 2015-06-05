from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    caption = models.CharField(max_length=80)
    user = models.ForeignKey(User)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    content = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.caption, self.user, self.content)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=())
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user

class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name






