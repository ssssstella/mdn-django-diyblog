from django.test import TestCase
from django.urls import reverse

from blog.models import Blog, Author, BlogComment

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 5 authors for pagination tests
        number_of_authors = 5

        for author_id in range(number_of_authors):
            Author.objects.create(
                name=f'name {author_id}',
                bio=f'bio {author_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/author_list.html')

class AuthorDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 5 authors for pagination tests
        cls.test_author = Author.objects.create(
                            name='author name',
                            bio='author bio',
                         )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/blog/blogger/{self.test_author.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/author_detail.html')

class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 8 blogs for pagination tests
        number_of_blogs = 8
        test_author = Author.objects.create(name='John', bio='This is bio')

        for blog_id in range(number_of_blogs):
            Blog.objects.create(
                title=f'Title {blog_id}',
                description=f'Description {blog_id}',
                author=test_author
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 5)

    def test_lists_all_blogs(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 3)

class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test blog
        test_author = Author.objects.create(name='John', bio='This is bio')
        cls.test_blog = Blog.objects.create(
                            title='Blog Title',
                            description='Blog Description',
                            author=test_author
                        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/blog/blog/{self.test_blog.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk': self.test_blog.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk': self.test_blog.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')


import datetime
from django.utils import timezone
# Get user model from settings
from django.contrib.auth import get_user_model
User = get_user_model()

class BlogCommentCreateViewTest(TestCase):
    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        # Create an author and a blog
        test_author = Author.objects.create(name='John', bio='This is bio')
        
        self.test_blog = Blog.objects.create(
                title='Blog Title',
                description='Blog Description',
                author=test_author
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('create-comment-user', kwargs={'pk': self.test_blog.pk}))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('create-comment-user', kwargs={'pk': self.test_blog.pk}))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'blog/blogcomment_form.html')