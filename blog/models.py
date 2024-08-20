from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import datetime

class Blog(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    # Foreign Key used because blog can only have one author, but authors can have multiple blog posts.
    # Author as a string rather than object because it hasn't been declared yet in file.

    description = models.TextField(
        max_length=5000, help_text="Enter the description of the blog post")
    
    post_date = models.DateField(default=datetime.date.today())

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])

import uuid # Required for unique book instances

class BlogComment(models.Model):

    """Model representing a specific comment of a blog."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular comment")
    username = models.CharField(max_length=100)
    blog = models.ForeignKey('blog', on_delete=models.RESTRICT, null=True)
    description = models.TextField(
        max_length=1000, help_text="Enter comment about blog here.")
    
    post_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['post_datetime']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.blog.title})'

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    bio = models.TextField(
        max_length=1000, help_text="Enter the bio of the author")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


