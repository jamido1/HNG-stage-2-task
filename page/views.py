from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return redirect("page:homepage")
    return render(request, 'page/homepage.html', {})



