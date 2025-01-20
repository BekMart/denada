from django.shortcuts import render
from home.models import Restaurant
from .models import Time, Address, Contact, Social

# Create your views here.
def contact_page(request):
    print("About to render template")

    latest_details = Restaurant.objects.latest('updated_on')
    latest_time = Time.objects.latest('updated_on')
    latest_address = Address.objects.latest('updated_on')
    latest_contact = Contact.objects.latest('updated_on')
    latest_social = Social.objects.latest('updated_on')

    context = {
        'details': latest_details,
        'time': latest_time,
        'address': latest_address,
        'contact': latest_contact,
        'social': latest_social,
    }

    return render(
        request,
        "contact/contact.html",
        context
    )