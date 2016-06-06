from .models import Post
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_size', 'created_at']

    def content_size(self, post):
        return '%s자' % intcomma(len(post.content))

admin.site.register(Post, PostAdmin)