from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Item, Image, New
from .forms import AddSaloon, Images, IMG, News
from django.http import HttpResponse
import time


# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)


def checkout(request):
    return render(request, "checkout.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home.html"


# def add_gallery(request):
#     if request.method == "POST":
#         form = Images(request.POST, request.FILES)
#         if form.is_valid():
#             img = request.POST.get("Image")
#             post = form.save(commit=False)
#             post.save()
#             Img = Image(
#                 image=img
#             )
#             Img.save()
#             return redirect("../")
#     else:
#         return render(request, "add_image.html", {"form": Images()})

def add_gallery(request):
    if request.method == 'POST':
        form = IMG(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("../")
    else:
        form = IMG()
    return render(request, "add_image.html", {"form": IMG()})


def add_new(request):
    if request.method == 'POST':
        form = News(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("../")
    else:
        form = News()
    return render(request, "add_new.html", {"form": News()})


def add(request):
    if request.method == 'POST':
        form = AddSaloon(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("../")
    else:
        form = AddSaloon()
    return render(request, "add_image.html", {"form": AddSaloon()})

# def add(request):
#     if request.method == "POST":
#         Title = request.POST.get("Title")
#         Price = request.POST.get("Price")
#         Discount_Price = request.POST.get("Discount_Price")
#         Сategory = request.POST.get("Сategory")
#         Description = request.POST.get("Description")
#         Info = request.POST.get("Info")
#         Image = request.POST.get("Image")
#         Image1 = request.POST.get("Image1")
#         Image2 = request.POST.get("Image2")
#         Image3 = request.POST.get("Image3")
#         Image4 = request.POST.get("Image4")
#         Image5 = request.POST.get("Image5")
#         Image6 = request.POST.get("Image6")
#         Image7 = request.POST.get("Image7")
#         Image8 = request.POST.get("Image8")
#         Saloon = Item(
#             title=Title,
#             price=Price,
#             discount_price=Discount_Price,
#             category=Сategory,
#             slug=str(int(time.time())),
#             description=Description,
#             info=Info,
#             image=Image,
#             image1=Image1,
#             image2=Image2,
#             image3=Image3,
#             image4=Image4,
#             image5=Image5,
#             image6=Image6,
#             image7=Image7,
#             image8=Image8,
#             status=False
#         )
#         Saloon.save()
#         return redirect("../")
#     else:
#         return render(request, "add.html", {"form": AddSaloon()})


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


class ItemModer(ListView):
    model = Item
    template_name = "moder_saloon.html"


class ImgModer(ListView):
    model = Image
    template_name = "moder_image.html"


class NewsModer(ListView):
    model = New
    template_name = "moder_news.html"


class ServiceView(ListView):
    model = Item
    template_name = "Service.html"


class ServiceView(ListView):
    model = Item
    template_name = "Service.html"


class NewsView(ListView):
    model = New
    template_name = "news.html"


class GalleryView(ListView):
    model = Image
    template_name = "gallery.html"


class ProfileView(ListView):
    model = Item
    template_name = "profile.html"


class AboutView(ListView):
    model = Item
    template_name = "about.html"
