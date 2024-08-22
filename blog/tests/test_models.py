from django.test import TestCase

from blog.models import Blog, Author, BlogComment

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(name='Bob')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
    
    def test_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = author.name
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/blog/blogger/1')

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_author = Author.objects.create(name='Bob')
        Blog.objects.create(
            title='test blog post',
            author=test_author,
            description='my blog summary'
        )

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)
    
    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEqual(max_length, 5000)
    
    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEqual(str(blog), expected_object_name)

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blog.get_absolute_url(), '/blog/blog/1')

import uuid
class BlogCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_author = Author.objects.create(name='Bob')
        test_blog = Blog.objects.create(
            title='test blog post',
            author=test_author,
            description='my blog summary'
        )
        cls.test_blogcomment = BlogComment.objects.create(
            id=uuid.uuid4(),
            blog=test_blog,
            description="comment no.1"
        )

    def test_description_label(self):
        field_label = self.test_blogcomment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        max_length = self.test_blogcomment._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)
    
    def test_post_datetime_label(self):
        field_label = self.test_blogcomment._meta.get_field('post_datetime').verbose_name
        self.assertEqual(field_label, 'post datetime')

    def test_object_name_is_id_plus_blog_title(self):
        expected_object_name = f'{self.test_blogcomment.id} ({self.test_blogcomment.blog.title})'
        self.assertEqual(str(self.test_blogcomment), expected_object_name)



