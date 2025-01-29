const editButtons = document.getElementsByClassName("btn-edit");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");

    // Get the hidden input field in the form
    const bookingIdInput = document.getElementById("booking_id"); 

    // Set the value of the hidden input field
    if (bookingIdInput) {
      bookingIdInput.value = bookingId; 
    }

    // Submit the form
    bookingForm.submit(); 
  });
}

// Initialised deletion functionality for all `deleteButtons`
// Selects associated booking ID when clicked
// Goes to cancel_booking href for specific booking
// Displays `deleteModal` to confirm user wishes to cancel

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
    deleteConfirm.href = `cancel_booking/${bookingId}`;
    deleteModal.show();
  });
}