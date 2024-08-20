from django.contrib import admin

# Register your models here.
from .models import Author, Blog, BlogComment

admin.site.register(Author)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('display_comment_name', 'username', 'post_datetime', 'id')

    def display_comment_name(self, obj):
        """Create a comment name truncating the comment description to 75 characters."""
        return obj.description[:75]
    
    display_comment_name.short_description = 'name'

admin.site.register(BlogComment, BlogCommentAdmin)

class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]
