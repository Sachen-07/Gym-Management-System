document.getElementById('membershipForm').addEventListener('submit', function(event) {
    let isValid = true;

    // Clear previous errors
    document.querySelectorAll('.error').forEach(function(error) {
        error.textContent = '';
    });

    // Name validation
    const name = document.getElementById('name').value;
    if (name.trim() === '') {
        document.getElementById('nameError').textContent = 'Full Name is required.';
        isValid = false;
    }

    // Email validation
    const email = document.getElementById('email').value;
    const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    if (!emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        isValid = false;
    }

    // Age validation
    const age = document.getElementById('age').value;
    if (age <= 0 || age.trim() === '') {
        document.getElementById('ageError').textContent = 'Please enter a valid age.';
        isValid = false;
    }

    // Phone validation
    const phone = document.getElementById('phone').value;
    const phonePattern = /^\d{10}$/; // Example pattern for 10-digit phone number
    if (!phonePattern.test(phone)) {
        document.getElementById('phoneError').textContent = 'Please enter a valid phone number.';
        isValid = false;
    }

    // Gender validation
    const gender = document.getElementById('gender').value;
    if (gender === '') {
        document.getElementById('genderError').textContent = 'Please select a gender.';
        isValid = false;
    }

    // Membership validation
    const membership = document.getElementById('membership').value;
    if (membership === '') {
        document.getElementById('membershipError').textContent = 'Please select a membership type.';
        isValid = false;
    }

    // If form is not valid, prevent submission
    if (!isValid) {
        event.preventDefault();
    }
});