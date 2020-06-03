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
    ItemModer
)
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service/', ServiceView.as_view(), name='service'),
    path('news/',  NewsView.as_view(), name='news'),
    path('gallery/',  GalleryView.as_view(), name='gallery'),
    path('about/',  AboutView.as_view(), name='about'),
    path('profile/',  ProfileView.as_view(), name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('add/', add, name='add'),
    path('moder_saloon/', ItemModer.as_view(), name='moder_saloon'),


    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]
