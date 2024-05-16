from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=50, default='Anonymous')

    def __str__(self):
        return self.title