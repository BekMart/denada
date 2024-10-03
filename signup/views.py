from django.shortcuts import render

# Create your views here.
def signup_page(request):
    print("About to render template")

    return render(
        request,
        "signup/signup.html",
    )