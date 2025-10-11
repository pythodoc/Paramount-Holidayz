from django.shortcuts import render
from django.core.mail import send_mail

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
            inquiry = form.save()
            # Send email notification
            subject = f'New Inquiry from {inquiry.name}'
            message = f"""
New inquiry received:

Name: {inquiry.name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Message: {inquiry.message}

Submitted on: {inquiry.created_at}
"""
            from_email = 'india@paramountholidayz.com'  # Replace with your email
            recipient_list = ['india@paramountholidayz.com']  # Replace with admin email
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                # Log error if email fails, but don't break the form submission
                print(f"Email sending failed: {e}")
            return render(request, 'contact.html', {'form': InquiryForm(), 'message': 'Thank you for your inquiry! We will get back to you soon.'})
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def custom_package(request):
    return render(request, 'custom_package.html')