from django.shortcuts import render
from .models import About, Produce, Visit


def homepage(request):
    """
    Renders the landing page with the latest about, produce, and visit details.
    - Takes the incoming request object.
    - Returns the most recently updated records for the about section, produce,
    and visit details, and passes them to the homepage template.
    """
    # Retrieve the latest updated details for the homepage sections
    latest_about = About.objects.latest('updated_on')
    latest_produce = Produce.objects.latest('updated_on')
    latest_visit = Visit.objects.latest('updated_on')

    # Context dictionary to pass data to the template
    context = {
        'about': latest_about,
        'produce': latest_produce,
        'visit': latest_visit,
    }

    # Render and return the homepage with the latest details
    return render(
        request,
        "home/index.html",
        context
    )
