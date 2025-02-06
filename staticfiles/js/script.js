// document.addEventListener("DOMContentLoaded", () => {
//   // Get the close button element by ID or class
//   const closeButton = document.getElementById("closeButton");

//   // Check if the close button exists
//   if (closeButton) {
//     closeButton.addEventListener("click", () => {
//       console.log("Close button clicked!"); // Add any functionality you need here
//     });
//   } else {
//     console.warn("Close button not found in the DOM.");
//   }
// });


document.addEventListener("click", (event) => {
    if (event.target && event.target.classList.contains("btn-close")) {
      console.log("Close button clicked!");
    }
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
