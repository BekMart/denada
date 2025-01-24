from django.shortcuts import render

def handle_error_404(request, exception):
    return render(request, '404.html')