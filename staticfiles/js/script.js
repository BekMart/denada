// For slide navigation menu
// Select all elements with the class "sidenav"
const slide_menu = document.querySelectorAll(".sidenav");

// Initialize Materialize CSS Sidenav component for each selected element
M.Sidenav.init(slide_menu, {}); 

// To ensure that the alert closes when the close button is clicked
// Select the close button element with the class 'btn-close'
const closeButton = document.querySelector('.btn-close');

// Check if the closeButton exists before adding an event listener (`?.` prevents errors)
closeButton?.addEventListener('click', () => {
    // Find the closest parent element with the class 'alert'
    const alertElement = closeButton.closest('.alert');
    // Hide the alert by setting its display property to 'none'
    alertElement.style.display = 'none';
});