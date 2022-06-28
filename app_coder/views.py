import os
import random
import string
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from asyncore import read
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

from app_coder.models import Avatar, Blog, Profile
from app_coder.forms import AvatarForm, ProfileForm, BlogForm

from django.contrib import messages


def index(request):
    blogs = Blog.objects.all()
    
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx, 'blogs': blogs}

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html"
    )

def about_us(request):
    return render(request, 'app_coder/about_us.html')

def error(request):
    return render(request, 'app_coder/error.html')

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(autorName__contains=search_param), Q.OR)
        blogs = Blog.objects.filter(query)
        context_dict.update({
            'blogs': blogs
        })
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )



from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    model = Blog
    template_name = "app_coder/blog_list.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "app_coder/blog_detail.html"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('app_coder:blog-list')
    fields = ['title', 'subTitle','autorName','autorSurname', 'fecha', 'cuerpo', 'image']

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('app_coder:blog-list')
    fields = ['title', 'subTitle','autorName','autorSurname', 'fecha', 'cuerpo', 'image']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('app_coder:blog-list')

class ProfileListView(ListView):
    model = Profile
    template_name = "app_coder/profile_list.html"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "app_coder/profile_detail.html"

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy('app_coder:profile-list')
    fields = ['nombre', 'descripcion', 'email', 'image', 'link']

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy('app_coder:profile-list')
    fields = ['nombre', 'descripcion', 'email', 'image', 'link']

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('app_coder:profile-list')


from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from app_coder.forms import UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("app_coder:user-login")
    # form = UserCreationForm()
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="app_coder/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("app_coder:Home")

        return render(
            request=request,
            context={'form': form},
            template_name="app_coder/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("app_coder:user-login")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return redirect('app_coder:Home')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('app_coder:Home')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_coder/avatar_form.html",
    )

@login_required
def profile_load(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            profiles = Profile.objects.filter(user=request.user.id)
            if not profiles.exists():
                profile = Profile(user=request.user, image=image)
            else:
                profile = profile[0]
                if len(profile.image) > 0:
                    os.remove(profile.image.path)
                profile.image = image
            profile.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('app_coder:Home')

    form= ProfileForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_coder/profile_form.html",
    )

@login_required
def blog_load(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            blogs = Blog.objects.filter(user=request.user.id)
            if not blogs.exists():
                blog = Blog(user=request.user, image=image)
            else:
                blog = blog[0]
                if len(blog.image) > 0:
                    os.remove(blog.image.path)
                blog.image = image
            blog.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('app_coder:Home')

    form= BlogForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_coder/blog_form.html",
    )