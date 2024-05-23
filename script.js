function sendMessage() {
    // Function for sending messages to the chat interface
    // This function can remain the same as before
}

function submitQuestion() {
    const questionText = document.getElementById('questionText').value;
    const videoFile = document.getElementById('videoUpload').files[0];

    // Create a FormData object to send the question and video file
    const formData = new FormData();
    formData.append('question_text', questionText);
    formData.append('video', videoFile);

    // Send the data to the backend using fetch API
    fetch('/submit_question', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        console.log('Question submitted successfully:', result);
        showNotification('Question Submitted', 'Your question has been submitted successfully');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function showNotification(title