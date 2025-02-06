from django.shortcuts import render


def handle_error_404(request):
    """
    Handles 404 Page Not Found errors.
    This view is triggered when a requested page is not found for better user experience.
    - Takes the incoming request object.
    - Returns the rendered 404 error page.
    """
    return render(
        request,
        '404.html'
    )
