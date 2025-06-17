from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render (request, "index.html")
    # return HttpResponse("This is a homepage")
    
def summerScoop(request):
    return render (request, "summerScoop.html")
    # return HttpResponse("This is a homepage")

def about(request):
    return render(request, "about.html" )

    # return HttpResponse("this is about page")

def services(request):
    return render(request, "services.html" )

    # return HttpResponse("This is a service page")

def contact(request):
    return render(request, "contact.html" )

    # return HttpResponse("Hit me up")

def signIn(request):
    return render(request, "signIn.html")

# sign up 
def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = UserCreationForm()
    context = {'form': form}
    return render(request, "signUp.html", context)