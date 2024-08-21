from typing import Any
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
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse

class BlogCommentCreateView(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ["description"]

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.user = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        self.success_url = reverse('blog-detail', kwargs={'pk': self.kwargs['pk']})
        return super(BlogCommentCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogCommentCreateView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context