from django.forms import ModelForm
from blog.models import BlogComment

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CreateCommentForm(ModelForm):
    def clean_description(self):
        data = self.cleaned_data['description']

        # Check if data is empty.
        if (not data):
            raise ValidationError(_('Invalid comment - comment is empty'))

        # Remember to always return the cleaned data.
        return data
    
    class Meta:
        model = BlogComment
        fields = ['description']
        help_texts = {'description': _('Enter comment about blog here.')}
