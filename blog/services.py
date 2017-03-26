from .models import BlogPost, Tag, Comment
from django.core.validators import validate_email

def create_blog_post(*,
                     title,
                     content,
                     tags=None):
    errors = []

    if not title.strip():
        errors.append('Title is required.')

    if not content.strip():
        errors.append('Content is required.')

    if errors:
        return None, errors

    post = BlogPost.objects.create(title=title, content=content)

    for tag in Tag.objects.filter(id__in=tags):
        post.tags.add(tag)

    post.save()

    return post, None


def create_comment(email,
                     content,
                     id):
    errors = []


    if not email.strip():
        errors.append('Invalid Email is required.')

    if not content.strip():
        errors.append('Content is required.')

    if not id.strip():
        errors.append('Blogpost id is required.')

    if errors:
        return None, errors
    newblogId = BlogPost.objects.get(id=id)
    comentar = Comment.objects.create(email=email, content=content,blogpost=newblogId)
   # comentar.blogpost = blogId.id.int()
    comentar.save()

    return comentar, None
