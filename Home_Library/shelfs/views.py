from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, CreateView, ListView
from django.contrib.auth import get_user_model, login, logout, authenticate


from .models import Item, User
from .forms import LoginForm, CreateUserForm


# Create your views here.

class Library(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'shelfs/item_list.html'



class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'shelfs/user_list.html'


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