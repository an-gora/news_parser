from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    image = models.ImageField(upload_to='news/images/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}: {self.text}'

# Create your models here.
class Model:
    pass