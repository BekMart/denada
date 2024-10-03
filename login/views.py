from django.shortcuts import render

# Create your views here.
def login_page(request):
    print("About to render template")

    return render(
        request,
        "login/login.html",
    )