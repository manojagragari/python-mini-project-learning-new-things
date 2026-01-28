document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorDiv = document.getElementById('error');
    
    if (username === '' || password === '') {
        errorDiv.textContent = 'Please fill in all fields.';
    } else {
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Login successful!');
                // Optionally redirect: window.location.href = '/dashboard';
            } else {
                errorDiv.textContent = 'Invalid credentials.';
            }
        })
        .catch(error => {
            errorDiv.textContent = 'An error occurred. Please try again.';
        });
        errorDiv.textContent = '';
    }
});