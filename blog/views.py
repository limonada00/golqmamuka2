from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BlogPost, Tag, Comment
from .forms import BlogPostCreateModelForm, LoginForm
from .services import create_blog_post,create_comment
from .decorators import anonymous_required



def index(request):
    #if not request.session.get('counter'):
    #    request.session['counter'] = 0

    #request.session['counter'] += 1

    posts = BlogPost.objects.all()
    comments = Comment.objects.all()
   
    return render(request, 'blog/index.html', locals())

@login_required(login_url=reverse_lazy('users:login'))
def create_blog_post(request):
    form = BlogPostCreateModelForm()

    if request.method == 'POST':
        form = BlogPostCreateModelForm(data=request.POST)

        if form.is_valid():
            create_blog_post(**form.cleaned_data)
            return redirect(reverse('blog:index'))

    return render(request, 'blog/create.html', locals())


def blog_detail(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = request.POST.get('tags')
        postid = update_posts(title,content,tag,id)
        blog_posts = BlogPost.objects.all()
        url = reverse('index-page')
        return redirect(url)

    try:
        posts = BlogPost.objects.get(id=id)
    except posts.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    added_tags = Tag.objects.filter(posts=id)
    tags = Tag.objects.all()
    added_comments = Comment.objects.filter(blogpost=id)
    return render(request, 'blog/blog_post.html', locals())
    

def blog_detailform(request, id):
    if request.method == 'POST':
        email = request.POST.get('senderEmail')

        content = request.POST.get('comment')

        commentsid = create_comment(email,content,id)
        added_comments = Comment.objects.filter(blogpost=id)
        return render(request, 'blog/blog_post.html', locals())
        #url = reverse('index-page')
        #return redirect(url)

    try:
        posts = BlogPost.objects.get(id=id)
    except posts.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    added_tags = Tag.objects.filter(posts=id)
    tags = Tag.objects.all()
    added_comments = Comment.objects.filter(blogpost=id)
    return render(request, 'blog/blog_post.html', locals())


@anonymous_required(profile_url=reverse_lazy('blog:profile'))
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is None:
                form.add_error(field='', error='No such user')
            else:
                login(request, user)

    return render(request, 'blog/login.html', locals())


@login_required(login_url=reverse_lazy('blog:index'))
def profile_view(request):
    return render(request, 'blog/profile.html', locals())



# login_required_views = [profile_view]


# for view in login_required_views:
#     fname = view.__name__
#     local_definitions = locals()

#     f = local_definitions.get(fname)

#     f = login_required(f)

#     local_definitions[fname] = f

