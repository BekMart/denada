const editButtons = document.getElementsByClassName("btn-edit");

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