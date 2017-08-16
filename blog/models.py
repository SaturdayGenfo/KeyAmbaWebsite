from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    saying = models.TextField()
    description = models.TextField()
    def __unicode__(self):
        return self.saying

class Comment(models.Model):
    poster = models.TextField()
    text = models.TextField()
    post = models.ForeignKey('Post')

    def __unicode__(self):
        return self.poster
