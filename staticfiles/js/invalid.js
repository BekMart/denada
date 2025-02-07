// Get the input for the below elements by their ID's
const partyInput = document.getElementById('id_party_size');
const dateInput = document.getElementById('id_date');
const timeInput = document.getElementById('id_time');

// Remove the 'is-invalid' class from the listed inputs
// Used to clear the built in validation error styles
partyInput.classList.remove('is-invalid'); 
dateInput.classList.remove('is-invalid'); 
timeInput.classList.remove('is-invalid'); 