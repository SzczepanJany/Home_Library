from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth import get_user_model, login, logout, authenticate


from .models import Item, Publisher, Serie, User, Genre
from .forms import LoginForm, CreateUserForm, CreateNewItemForm, CreateNewGenreForm, CreateNewSerieForm, CreateNewPublisherForm, CreateNewRateForm


# Create your views here.


class GenreListView(ListView):
    form_class = CreateNewGenreForm
    model = Genre
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context

class SerieDetailView(DetailView):
    model = Serie
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        context['all_fields'] = Publisher._meta.get_fields()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Przedmiot: '
        context['url'] = 'item'
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Użytkownik: '
        context['url'] = 'user'
        return context


class PublisherDeleteView(DeleteView):
    template_name = 'shelfs/delete.html'
    model = Publisher
    context_object_name = 'item'
    success_url = reverse_lazy('list_serie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        return context


class UserDeleteView(DeleteView):
    template_name = 'shelfs/delete.html'
    model = User
    context_object_name = 'item'
    success_url = reverse_lazy('list_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Użytkownik: '
        context['url'] = 'user'
        return context


class SerieDeleteView(DeleteView):
    template_name = 'shelfs/delete.html'
    model = Serie
    context_object_name = 'item'
    success_url = reverse_lazy('list_serie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class GenreDeleteView(DeleteView):
    template_name = 'shelfs/delete.html'
    model = Genre
    success_url = reverse_lazy('list_genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context


class ItemDeleteView(DeleteView):
    template_name = 'shelfs/delete.html'
    model = Item
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Pozycja: '
        context['url'] = 'item'
        return context


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Pozycja: '
        context['url'] = 'item'
        return context


class SerieListView(ListView):
    model = Serie
    context_object_name = 'items'
    template_name = 'shelfs/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        return context

class UserListView(ListView):
    model = User
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Użytkownik: '
        context['url'] = 'user'
        return context


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
                return redirect('/list_items/')
            else:
                return render(request, 'shelfs/main.html', {'form': form})
        else:
            return render(request, 'shelfs/main.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_user')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        #breakpoint()
        return super().form_valid(form)


class CreateNewItemView(CreateView):
    form_class = CreateNewItemForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        item = form.save()
        item.save()
        #breakpoint()
        return super().form_valid(form)
        

class CreateNewGenreView(CreateView):
    form_class = CreateNewGenreForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_genre')

    def form_valid(self, form):
        genre = form.save()
        genre.save()
        #breakpoint()
        return super().form_valid(form)


class CreateNewSerieView(CreateView):
    form_class = CreateNewSerieForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_serie')

    def form_valid(self, form):
        serie = form.save()
        serie.save()
        return super().form_valid(form)


class CreateNewPublisherView(CreateView):
    form_class = CreateNewPublisherForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_publish')

    def form_valid(self, form):
        publisher = form.save()
        publisher.save()
        return super().form_valid(form)


class CreateNewRateView(CreateView):
    form_class = CreateNewRateForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        
        item = Item.objects.get(id=self.kwargs.get('pk'))
        form.instance.item = item
        user = User.objects.get(id=self.request.user.id)
        
        form.instance.user = user
        rate = form.save()
        rate.save()
        return super().form_valid(form)


class EditItemView(UpdateView):
    form_class = CreateNewItemForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('index')
    model = Item


class EditGenreView(UpdateView):
    form_class = CreateNewGenreForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_genre')
    model = Genre


class EditPublisherView(UpdateView):
    form_class = CreateNewPublisherForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_publish')
    model = Publisher


class EditSerieView(UpdateView):
    form_class = CreateNewSerieForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_serie')
    model = Serie


class EditUserView(UpdateView):
    form_class = CreateUserForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_user')
    model = User