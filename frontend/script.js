function uploadImage() {
    const input = document.getElementById('imageInput');
    const message = document.getElementById('message');

    if (input.files.length === 0) {
        message.innerText = "Please select an image.";
        return;
    }

    const formData = new FormData();
    formData.append('file', input.files[0]);

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            message.innerText = "Error: " + data.error;
        } else {
            message.innerText = "Success: " + data.success;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        message.innerText = "An error occurred while uploading.";
    });
}
