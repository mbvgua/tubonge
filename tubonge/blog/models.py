from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# create a custom model manager
class PublishedManager(models.Manager):
    """return all posts with a published status"""
    def get_queryset(self):
        # return super().get_queryset().filter(status=Post.Status.PUBLISHED)
        return super().get_queryset() \
            .filter(status=Post.Status.PUBLISHED)
    
class DateManager(models.Manager):
    """returns all posts ordering them by date published"""
    def get_queryset(self):
        return super().get_queryset().order_by('publish')



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft' 
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts',)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)


    objects = models.Manager() #default manager.if none specified its selected automatically
    published = PublishedManager() #custom manager
    date = DateManager() #custom manager

    # order blogs chronologically
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),  #index publish field
        ]

    # return human readable name whe queried
    def __str__(self):
        return self.title
    
    # using canonical urls
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug,])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields = ['created']),]

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"