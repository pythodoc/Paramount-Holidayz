from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    from .models import Service
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    from .forms import InquiryForm
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': InquiryForm(), 'message': 'Thank you for your inquiry!'})
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def custom_package(request):
    return render(request, 'custom_package.html')