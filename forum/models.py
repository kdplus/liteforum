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
    click_count = models.IntegerField(default=0)
    vedio_count = models.IntegerField(default=0)
    vedio_xml_link = models.CharField(max_length=200, default=None)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.caption, self.user, self.content,self.vedio_xml_link)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=())
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name
