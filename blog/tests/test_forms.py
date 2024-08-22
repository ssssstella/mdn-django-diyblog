from django.test import TestCase

from blog.forms import CreateCommentForm

class CreateCommentFormTest(TestCase):
    def test_create_comment_form_description_field_label(self):
        form = CreateCommentForm()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'Description')

    def test_create_comment_form_description_field_help_text(self):
        form = CreateCommentForm()
        self.assertEqual(form.fields['description'].help_text, 'Enter comment about blog here.')

    def test_create_comment_form_description_in_empty(self):
        description = ''
        form = CreateCommentForm(data={'description': description})
        self.assertFalse(form.is_valid())

   
