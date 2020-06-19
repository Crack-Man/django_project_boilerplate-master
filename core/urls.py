from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    ServiceView,
    NewsView,
    News,
    GalleryView,
    AboutView,
    ProfileView,
    add,
    add_gallery,
    add_new,
)
from .models import Item
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service/', ServiceView.as_view(), name='service'),
    path('news/',  News.as_view(), name='news'),
    path('news/add/', add_new, name='add_new'),
    path('gallery/',  GalleryView.as_view(), name='gallery'),
    path('gallery/add/',  add_gallery, name='add_image'),
    path('about/',  AboutView.as_view(), name='about'),
    path('profile/',  ProfileView.as_view(), name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('add/', add, name='add'),


    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('news/post/<slug>/', NewsView.as_view(), name='posts')
]
