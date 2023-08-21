from .forms import DemoForm
from django.shortcuts import render
from menuapp.forms import LogForm
from django.http import HttpResponse
from .models import Menu

# Create your views here.
def demo_form_view(request):
    form = DemoForm()
    return render(request, 'demo_form.html', {'form': form})

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)

def about(request):
    about_content = {'about': 'Here will be information about the company'}
    return render(request, 'about.html', about_content)

# def menu(request):
#     newmenu = {'mains': [
#         {"name": "Margarita", "price": "12"},
#         {"name": "Tequila-boom", "price": "5"},
#         {"name": "Mojito", "price": "9"},
#         {"name": "Long Island Ice Tea", "price": "16"}
#         ]}
#     return render(request, 'menu.html', newmenu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

def home(request): 
    return render(request, "home.html", {}) 
def about(request): 
    return render(request, "about.html", {})
def menu(request): 
    return render(request, "menu.html", {})
# def register(request): 
#     return render(request, "register.html", {}) 
# def login(request): 
#     return render(request, "login.html", {}) 