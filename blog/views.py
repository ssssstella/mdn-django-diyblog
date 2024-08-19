from django.shortcuts import render

# Create your views here.
from .models import Blog, Author, BlogComment

def index(request):
    """View function for home page of the site."""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()
    num_comments = BlogComment.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in context
    return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog


