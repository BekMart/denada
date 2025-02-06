from django.shortcuts import render
from home.models import Restaurant
from .models import Time, Address, Contact, Social


def contact_page(request):
    """
    Renders the contact page with the latest restaurant details.
    - Takes the incoming request object.
    - Fetches the most recently updated records for the restaurant's details.
    - Including business hours, address, contact information, and social media links.
    """

    # Retrieve the latest updated details for the restaurant
    latest_details = Restaurant.objects.latest('updated_on')
    latest_time = Time.objects.latest('updated_on')
    latest_address = Address.objects.latest('updated_on')
    latest_contact = Contact.objects.latest('updated_on')
    latest_social = Social.objects.latest('updated_on')

    # Context dictionary to pass data to the template
    context = {
        'details': latest_details,
        'time': latest_time,
        'address': latest_address,
        'contact': latest_contact,
        'social': latest_social,
    }

    # Render and return the contact page with the latest details
    return render(
        request,
        "contact/contact.html",
        context
    )
