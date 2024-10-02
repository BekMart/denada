from django.shortcuts import render

# Create your views here.
def booking_page(request):
    print("About to render template")

    return render(
        request,
        "book/book.html",
    )