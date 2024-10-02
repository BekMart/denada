from django.shortcuts import render

# Create your views here.
def menu_page(request):
    print("About to render template")

    return render(
        request,
        "menu/menu.html",
    )