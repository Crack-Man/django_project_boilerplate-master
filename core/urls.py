from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    ServiceView,
    NewsView,
    GalleryView,
    AboutView,
    ProfileView,
    add,
    ItemModer,
    ImgModer,
    NewsModer,
    add_gallery,
    add_new
)
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service/', ServiceView.as_view(), name='service'),
    path('news/',  NewsView.as_view(), name='news'),
    path('news/add/', add_new, name='add_new'),
    path('gallery/',  GalleryView.as_view(), name='gallery'),
    path('gallery/add/',  add_gallery, name='add_image'),
    path('about/',  AboutView.as_view(), name='about'),
    path('profile/',  ProfileView.as_view(), name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('add/', add, name='add'),
    path('moder/saloon/', ItemModer.as_view(), name='moder_saloon'),
    path('moder/image/', ImgModer.as_view(), name='moder_image'),
    path('moder/news/', NewsModer.as_view(), name='moder_image'),


    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]
