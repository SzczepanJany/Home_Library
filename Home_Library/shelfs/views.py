from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone


from .models import Author, Item, Publisher, Serie, User, Genre, UserItem, Loans
from .forms import CreateNewLentForm, CreateNewLoanForm, CreateNewReturnForm, LoginForm, CreateUserForm, CreateNewItemForm, CreateNewGenreForm, CreateNewSerieForm, CreateNewPublisherForm, CreateNewRateForm, CreateNewAuthorForm


# Create your views here.


class GenreListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_genre'
    login_url = reverse_lazy('main')
    form_class = CreateNewGenreForm
    model = Genre
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context


class GenreDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_genre'
    login_url = reverse_lazy('main')
    model = Genre
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context


class SerieDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_serie'
    login_url = reverse_lazy('main')
    model = Serie
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class PublisherDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_publisher'
    login_url = reverse_lazy('main')
    model = Publisher
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        context['all_fields'] = Publisher._meta.get_fields()
        return context


class ItemDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_item'
    login_url = reverse_lazy('main')
    model = Item
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Przedmiot: '
        context['url'] = 'item'
        return context


class UserDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_user'
    login_url = reverse_lazy('main')
    model = User
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Użytkownik: '
        context['url'] = 'user'
        return context


class AuthorDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shelfs.view_author'
    login_url = reverse_lazy('main')
    model = Author
    template_name = 'shelfs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Autor: '
        context['url'] = 'authr'
        return context


class PublisherDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_publisher'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = Publisher
    context_object_name = 'item'
    success_url = reverse_lazy('list_serie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        return context


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_user'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = User
    context_object_name = 'item'
    success_url = reverse_lazy('list_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Użytkownik: '
        context['url'] = 'user'
        return context


class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_author'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = Author
    context_object_name = 'item'
    success_url = reverse_lazy('list_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Autor: '
        context['url'] = 'authr'
        return context


class SerieDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_serie'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = Serie
    context_object_name = 'item'
    success_url = reverse_lazy('list_serie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_genre'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = Genre
    success_url = reverse_lazy('list_genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Gatunek: '
        context['url'] = 'genre'
        return context


class ItemDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shelfs.delete_item'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/delete.html'
    model = Item
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Pozycja: '
        context['url'] = 'item'
        return context


class ItemListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_item'
    login_url = reverse_lazy('main')
    model = Item
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Pozycja: '
        context['url'] = 'item'
        return context


class AuthorListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_author'
    login_url = reverse_lazy('main')
    model = Author
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Autor: '
        context['url'] = 'authr'
        return context


class SerieListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_serie'
    login_url = reverse_lazy('main')
    model = Serie
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Seria: '
        context['url'] = 'serie'
        return context


class PublisherListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_publisher'
    login_url = reverse_lazy('main')
    model = Publisher
    context_object_name = 'items'
    template_name = 'shelfs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descr'] = 'Wydawca: '
        context['url'] = 'publish'
        return context


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'shelfs.view_user'
    login_url = reverse_lazy('main')
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
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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


class CreateUserView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_user'
    login_url = reverse_lazy('main')
    form_class = CreateUserForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_user')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        # breakpoint()
        return super().form_valid(form)


class CreateNewItemView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_item'
    login_url = reverse_lazy('main')
    form_class = CreateNewItemForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        item = form.save()
        user_item = UserItem.objects.create(user=user, item=item)
        user_item.favourite = form.cleaned_data['is_favourite']
        user_item.nr_of_copies = form.cleaned_data['nr_of_copies']
        # breakpoint()
        return super().form_valid(form)


class CreateNewAuthorView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_author'
    login_url = reverse_lazy('main')
    form_class = CreateNewAuthorForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_authr')

    def form_valid(self, form):
        item = form.save()
        item.save()
        # breakpoint()
        return super().form_valid(form)


class CreateNewGenreView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_genre'
    login_url = reverse_lazy('main')
    form_class = CreateNewGenreForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_genre')

    def form_valid(self, form):
        genre = form.save()
        genre.save()
        # breakpoint()
        return super().form_valid(form)


class CreateNewSerieView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_serie'
    login_url = reverse_lazy('main')
    form_class = CreateNewSerieForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_serie')

    def form_valid(self, form):
        serie = form.save()
        serie.save()
        return super().form_valid(form)


class CreateNewPublisherView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_publisher'
    login_url = reverse_lazy('main')
    form_class = CreateNewPublisherForm
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('list_publish')

    def form_valid(self, form):
        publisher = form.save()
        publisher.save()
        return super().form_valid(form)


class CreateNewRateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_rate'
    login_url = reverse_lazy('main')
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


class EditItemView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_item'
    login_url = reverse_lazy('main')
    form_class = CreateNewItemForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('index')
    model = Item

    def form_valid(self, form):
        response = super().form_valid(form)
        # does not exist
        # user = self.request.user
        try:
            us_it = UserItem.objects.get(item=self.object, user=self.request.user)
        except ObjectDoesNotExist:
            user_item = UserItem.objects.create(item=self.object, user=self.request.user)
        us_it.favourite = form.cleaned_data['is_favourite']
        us_it.nr_of_copies = form.cleaned_data['nr_of_copies']
        us_it.save()
        return response

    def get_initial(self):
        init_da = super().get_initial()
        try:
            init_da['is_favourite'] = UserItem.objects.get(item=self.object, user=self.request.user).favourite
        except ObjectDoesNotExist:
            user_item = UserItem.objects.create(item=self.object, user=self.request.user)
        init_da['nr_of_copies'] = UserItem.objects.get(item=self.object, user=self.request.user).nr_of_copies
        return init_da


class EditAuthorView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_author'
    login_url = reverse_lazy('main')
    form_class = CreateNewAuthorForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_authr')
    model = Author


class EditGenreView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_genre'
    login_url = reverse_lazy('main')
    form_class = CreateNewGenreForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_genre')
    model = Genre


class EditPublisherView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_publisher'
    login_url = reverse_lazy('main')
    form_class = CreateNewPublisherForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_publish')
    model = Publisher


class EditSerieView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_serie'
    login_url = reverse_lazy('main')
    form_class = CreateNewSerieForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_serie')
    model = Serie


class EditUserView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_user'
    login_url = reverse_lazy('main')
    form_class = CreateUserForm
    template_name = 'shelfs/edit.html'
    success_url = reverse_lazy('list_user')
    model = User


class CreateNewLoanView(PermissionRequiredMixin, CreateView):
    template_name = 'shelfs/add.html'
    permission_required = 'shelfs.add_loans'
    login_url = reverse_lazy('main')
    success_url = reverse_lazy('index')
    form_class = CreateNewLoanForm

    def form_valid(self, form):
        item = Item.objects.get(id=self.kwargs.get('pk'))
        form.instance.item = item
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        try:
            loa = Loans.objects.get(item=item, in_loans=True)
            return redirect('/list_items/')
        except ObjectDoesNotExist:
            form.instance.in_loans = True
            loan = form.save()
            loan.save()
            return super().form_valid(form)


class CreateNewLentView(PermissionRequiredMixin, CreateView):
    permission_required = 'shelfs.add_loans'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('index')
    form_class = CreateNewLentForm

    def form_valid(self, form):
        item = Item.objects.get(id=self.kwargs.get('pk'))
        form.instance.item = item
        try:
            loa = Loans.objects.get(item=item, in_loans=True)
            return redirect('/list_items/')
        except ObjectDoesNotExist:
            form.instance.in_loans = True
            loan = form.save()
            loan.save()
            return super().form_valid(form)


class CreateNewReturnView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shelfs.change_loans'
    login_url = reverse_lazy('main')
    template_name = 'shelfs/add.html'
    success_url = reverse_lazy('index')
    form_class = CreateNewReturnForm
    model = Loans

    def form_valid(self, form):
        lent = self.object
        user = self.request.user
        # breakpoint()
        if form.instance.user == user:
            lent.in_loans = False
            lent.date_of_return = timezone.now()
            lent.description = form.cleaned_data['description']
            lent.description = form.cleaned_data['file']
            lent.save()
            return super().form_valid(form)
        else:
            return redirect('/list_items/')
