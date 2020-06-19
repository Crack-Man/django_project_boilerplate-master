from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Item, Image, New, Recording
from .forms import AddSaloon, Images, IMG, NewsForm, Recordings
from django.http import HttpResponse
import time
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin

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
            new_post = form.save(commit=False)
            new_post.auth = request.user
            new_post.save()
            return redirect("../")
    else:
        form = IMG()
    return render(request, "add_image.html", {"form": IMG()})


def add_new(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auth = request.user
            new_post.slug = str(int(time.time()))
            new_post.save()
            return redirect("../")
    else:
        form = NewsForm()
    return render(request, "add_new.html", {"form": NewsForm()})


def add(request):
    if request.method == 'POST':
        form = AddSaloon(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auth = request.user
            new_post.slug = str(int(time.time()))
            new_post.save()
            return redirect("/../")
    else:
        form = AddSaloon()
    return render(request, "add.html", {"form": AddSaloon()})


    

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

class ItemDetailView(FormMixin, DetailView):
    model = Item
    form_class = Recordings
    initial = {'key': 'value'}
    template_name = "product.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auth = request.user
            slug = request.path[9 : len(request.path) - 1]
            new_post.title = slug
            new_post.save()
            return redirect("/../")
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = Recordings
        return context
    
class NewsView(DetailView):
    model = New
    template_name = "posts.html"

class ServiceView(ListView):
    model = Item
    template_name = "Service.html"


class ServiceView(ListView):
    model = Item
    template_name = "Service.html"


class News(ListView):
    model = New
    template_name = "news.html"


class GalleryView(ListView):
    model = Image
    template_name = "gallery.html"


class ProfileView(ListView):
    model = Recording
    template_name = "profile.html"


class AboutView(ListView):
    model = Item
    template_name = "about.html"
