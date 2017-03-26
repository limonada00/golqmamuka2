from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

#from .models import BlogPost, Tag
from .forms import LoginForm
#from . import services
from .decorators import anonymous_required


@anonymous_required(profile_url=reverse_lazy('users:profile'))
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
                return redirect(reverse('users:profile'))
                #return render(request, 'users/profile.html', locals())

    return render(request, 'users/login.html', locals())


@login_required(login_url=reverse_lazy('users:login'))
def profile_view(request):
    return render(request, 'users/profile.html', locals())


def logout_user(request):
    logout(request)
    return redirect(reverse('blog:index'))



# login_required_views = [profile_view]


# for view in login_required_views:
#     fname = view.__name__
#     local_definitions = locals()

#     f = local_definitions.get(fname)

#     f = login_required(f)

#     local_definitions[fname] = f

