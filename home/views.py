from django.shortcuts import render
from .models import Restaurant, About, Produce, Visit

# Create your views here.
def homepage(request):
    print("About to render template")

    latest_about = About.objects.latest('updated_on') 
    latest_produce = Produce.objects.latest('updated_on')
    latest_visit = Visit.objects.latest('updated_on')

    context = {
        'about': latest_about,
        'produce': latest_produce,
        'visit': latest_visit,
    }

    return render(
        request,
        "home/index.html",
        context
    )