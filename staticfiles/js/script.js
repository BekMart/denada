// For slide nav menu
const slide_menu = document.querySelectorAll(".sidenav");
M.Sidenav.init(slide_menu, {});
// To ensure that alert closes when close button clicked 
const closeButton = document.querySelector('.btn-close');
closeButton.addEventListener('click', () => {
    // Code to close the alert or perform other actions
    const alertElement = closeButton.closest('.alert');
    alertElement.style.display = 'none'; // Hide the alert
});