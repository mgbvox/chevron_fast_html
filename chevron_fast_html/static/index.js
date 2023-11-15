document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector('.centered-button');
    button.addEventListener('click', function() {
        fetch('/get-html')
            .then(response => response.text())
            .then(data => {
                document.body.innerHTML += data;
            })
            .catch(error => console.error('Error:', error));
    });
});
