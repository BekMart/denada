from django.shortcuts import render

# Create your views here.
def homepage(request):
    print("About to render template")

    return render(
        request,
        "home/index.html",
    )