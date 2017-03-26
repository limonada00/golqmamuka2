from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255, unique=True)

    tags = models.ManyToManyField(Tag,
                                  related_name='posts')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()
    author = models.ManyToManyField(User,
                                  related_name='authors')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)


class Comment(models.Model):
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=255)
    blogpost = models.ForeignKey(BlogPost, related_name='posts')