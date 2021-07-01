from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, CreateView, ListView
from django.contrib.auth import get_user_model, login, logout, authenticate


from .models import Item, Publisher, Serie, User, Genre
from .forms import LoginForm, CreateUserForm, CreateNewItemForm, CreateNewGenreForm, CreateNewSerieForm, CreateNewPublisherForm


# Create your views here.

class LibraryView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'shelfs/list_item.html'


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'shelfs/list_genre.html'


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'shelfs/list_item.html'


class SerieListView(ListView):
    model = Serie
    context_object_name = 'series'
    template_name = 'shelfs/list_serie.html'


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'
    template_name = 'shelfs/list_publish.html'


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'shelfs/list_user.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm
        return render(request, 'shelfs/main.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/main/')
            else:
                return render(request, 'shelfs/main.html', {'form': form})
        else:
            return render(request, 'shelfs/main.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("main")


class CreateUserView(CreateView):
    form_class = CreateUserForm
    #fields = ['username', 'password', 'password', 'email']
    #model = User
    template_name = 'shelfs/add_user.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        #breakpoint()
        return super().form_valid(form)


class CreateNewItemView(CreateView):
    form_class = CreateNewItemForm
    template_name = 'shelfs/add_item.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        item = form.save()
        item.save()
        #breakpoint()
        return super().form_valid(form)
        

class CreateNewGenreView(CreateView):
    form_class = CreateNewGenreForm
    template_name = 'shelfs/add_genre.html'
    success_url = reverse_lazy('genre_list')

    def form_valid(self, form):
        genre = form.save()
        genre.save()
        #breakpoint()
        return super().form_valid(form)


class CreateNewSerieView(CreateView):
    form_class = CreateNewSerieForm
    template_name = 'shelfs/add_serie.html'
    success_url = reverse_lazy('series_list')

    def form_valid(self, form):
        serie = form.save()
        serie.save()
        return super().form_valid(form)


class CreateNewPublisherView(CreateView):
    form_class = CreateNewPublisherForm
    template_name = 'shelfs/add_publish.html'
    success_url = reverse_lazy('publisher_list')

    def form_valid(self, form):
        publisher = form.save()
        publisher.save()
        return super().form_valid(form)
