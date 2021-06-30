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
    path('main/', shelf_view.Library.as_view(), name="index"),
    path('logout/', shelf_view.UserLogoutView.as_view(), name ='logout'),
    path('add_user/', shelf_view.CreateUserView.as_view(), name ='add_user'),
    path('add_item/', shelf_view.CreateNewItem.as_view(), name ='add_item'),
    path('add_genre/', shelf_view.CreateNewGenre.as_view(), name ='add_genre'),
    path('list_users/', shelf_view.UserListView.as_view(), name='user_list'),
    path('list_genres/', shelf_view.GenreListView.as_view(), name='genre_list'),
    path('', shelf_view.LoginView.as_view(), name="main"),
]
