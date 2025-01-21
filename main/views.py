from django.shortcuts import render


def services(request):
    return render(request, "main/services.html")
    
def store(request):
    return render(request, "main/store.html")
    
def contact(request):
    return render(request, "main/contact.html")