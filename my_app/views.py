from django.shortcuts import render, redirect
from my_app.models import *
from my_app.forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index_view(request):
    socials = SocialMedia.objects.all()
    context = {
        "socials": socials,
    }
    return render(request, 'index.html', context)


def contact_view(request):
    text = Contact.objects.all()
    form = ContactForm()
    services = Our_Services.objects.all()
    if request.method == "POST":
        print(form.errors)
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            service = form.cleaned_data.get("contact_service")
            print(form.errors)
            form.contact_service = service
            form.save()
            form = ContactForm()

    context = {
        'text': text,
        "form": form,
        "services": services,

    }
    return render(request, 'contact.html', context)


def about_view(request):
    title = About.objects.last()

    context = {
        'title': title
    }
    return render(request, 'about.html', context)


def portfolio_view(request):
    images = Portfolio.objects.all()

    context = {

        'images': images

    }
    return render(request, 'portfolio.html', context)


def service_view(request):
    services = Our_Services.objects.all()
    service = request.GET.get("myservice")
    if service is not None:
        services = services.filter(name__icontains=service)

    paginator = Paginator(services, 1)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {

        'services': services,
        'p':p,

    }

    return render(request, 'service.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    context = {}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
