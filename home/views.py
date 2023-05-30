from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
   return render(request, 'index.html')
   #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        print(name,email,phone,subject,'daattattatat<<<<<<<<<<<<<<<<<<<<<<')
        contact = Contact.objects.create(name=name, email=email, phone=phone, subject=subject, date = datetime.today())
        contact.save()
        return render(request, 'index.html')


    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")  
