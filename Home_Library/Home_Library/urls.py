"""Home_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from shelfs import views as shelf_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', shelf_view.LibraryView.as_view(), name="index"),
    path('', shelf_view.LoginView.as_view(), name="main"),
    path('logout/', shelf_view.UserLogoutView.as_view(), name ='logout'),
    path('add_user/', shelf_view.CreateUserView.as_view(), name ='add_user'),
    path('list_users/', shelf_view.UserListView.as_view(), name='list_user'),
    path('add_item/', shelf_view.CreateNewItemView.as_view(), name ='add_item'),
    path('list_items/', shelf_view.ItemListView.as_view(), name='list_item'),
    path('add_genre/', shelf_view.CreateNewGenreView.as_view(), name ='add_genre'),
    path('list_genres/', shelf_view.GenreListView.as_view(), name='list_genre'),
    path('add_series/', shelf_view.CreateNewSerieView.as_view(), name ='add_serie'),
    path('list_series/', shelf_view.SerieListView.as_view(), name='list_serie'),
    path('add_publish/', shelf_view.CreateNewPublisherView.as_view(), name ='add_publish'),
    path('list_publish/', shelf_view.PublisherListView.as_view(), name='list_publish'),
    #path('add_rate/', shelf_view.CreateNewRateView.as_view(), name ='add_rate'),
]
