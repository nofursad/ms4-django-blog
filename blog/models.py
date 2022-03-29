from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import cloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(  )

# Create your models here.
