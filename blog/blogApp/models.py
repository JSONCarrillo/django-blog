from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.contrib.auth.base_user import AbstractBaseUser

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.lower())
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
        
class Post(models.Model):


    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=100)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='uncategorized')
    article_hook = models.TextField()
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    image_alt = models.CharField(blank=True, null=True, max_length=50)

    class Meta():
        ordering = ['-post_date', '-id']

    def __str__(self):
        return self.title + " | " + str(self.author.first_name) + str(self.author.last_name)

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))

    def total_likes(self):
        return self.likes.count()

