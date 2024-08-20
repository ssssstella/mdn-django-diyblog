from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.AuthorListView.as_view(), name='authors'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
