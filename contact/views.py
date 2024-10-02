from django.shortcuts import render

# Create your views here.
def contact_page(request):
    print("About to render template")

    return render(
        request,
        "contact/contact.html",
    )