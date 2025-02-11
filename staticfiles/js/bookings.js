// Edit Booking Functinality
// Select all elements with the class "btn-edit"
const editButtons = document.getElementsByClassName("btn-edit");

// Get the booking form
const bookingForm = document.getElementById("bookingForm");
// Iterate through each edit button and add an event listener
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    // Retrieve the booking ID stored in the button's `booking_id` attribute
    let bookingId = e.target.getAttribute("booking_id");
    // Get the hidden input field in the form that stores the booking ID
    const bookingIdInput = document.getElementById("booking_id");
    // If the hidden input field exists, update its value with the selected booking ID
    if (bookingIdInput) {
      bookingIdInput.value = bookingId;
    }
    // Submit the form to process the booking update
    bookingForm.submit();
  });
}

// Delete Booking Functionality
// Initialize Bootstrap's modal instance for the delete confirmation modal
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
// Select all elements with the class "btn-delete"
const deleteButtons = document.getElementsByClassName("btn-delete");
// Get the delete confirmation button inside the modal
const deleteConfirm = document.getElementById("deleteConfirm");

// Iterate through each delete button and add an event listener
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    // Retrieve the booking ID stored in the button's `booking_id` attribute
    let bookingId = e.target.getAttribute("booking_id");
    // Update the delete confirmation button's `href` to include the correct booking ID
    // This directs the user to the correct cancellation link
    deleteConfirm.href = `cancel_booking/${bookingId}`;
    // Show the delete confirmation modal to ask the user for confirmation
    deleteModal.show();
  });
}
