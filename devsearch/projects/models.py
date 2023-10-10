from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Projects(models.Model):
    owner = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True , blank=True)
    profile_pic = models.ImageField(null=True,blank=True, default="default.jpg")
    tag = models.ManyToManyField('Tags', blank=True)
    demo_link = models.CharField(max_length=500,null=True,blank=True)
    source_link = models.CharField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

class Review(models.Model):
    owner = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class Tags(models.Model):
    name =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name