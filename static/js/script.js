document.addEventListener("DOMContentLoaded", () => {
    // Initialize Materialize side navigation
    const sidenav = document.querySelectorAll(".sidenav");
    const instances = M.Sidenav.init(sidenav);
  
    // Optionally, handle custom logic when the sidenav closes
    sidenav.forEach((nav) => {
      nav.addEventListener("click", (e) => {
        // Example: Detect clicks outside the sidenav or on specific elements
        if (e.target.classList.contains("sidenav-overlay")) {
          console.log("Sidenav closed!");
        }
      });
    });
  });

// // For slide nav menu
// const slide_menu = document.querySelectorAll(".sidenav");
// M.Sidenav.init(slide_menu, {});

// // To ensure that alert closes when close button clicked
// const closeButton = document.querySelector('.btn-close');
// closeButton.addEventListener('click', () => {
//     // Code to close the alert or perform other actions
//     const alertElement = closeButton.closest('.alert');
//     alertElement.style.display = 'none'; // Hide the alert
// });
