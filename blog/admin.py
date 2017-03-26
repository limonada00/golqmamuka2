from django.contrib import admin

from .models import BlogPost, Tag, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email','created','content', )
