//WORKS WELL & TRAINED


document.addEventListener('DOMContentLoaded', (event) => {

    document.getElementById('send-btn').addEventListener('click', function () {
        let userMessage = document.getElementById('chat-input').value;

        // Clear the input field
        document.getElementById('chat-input').value = '';

        // Append the user's message to the chatlogs
        let userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user';
        userMessageDiv.textContent = userMessage;
        document.getElementById('chatlogs').appendChild(userMessageDiv);

        // Scroll to the bottom
        document.getElementById('chatlogs').scrollTop = document.getElementById('chatlogs').scrollHeight;

        // Send the user's message to the backend and get the chatbot's response
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                let botMessage = data.message;

                // Append the chatbot's message to the chatlogs
                let botMessageDiv = document.createElement('div');
                botMessageDiv.className = 'message bot';
                botMessageDiv.textContent = botMessage;
                document.getElementById('chatlogs').appendChild(botMessageDiv);

                // Scroll to the bottom
                document.getElementById('chatlogs').scrollTop = document.getElementById('chatlogs').scrollHeight;
            })
            .catch(e => {
                console.log('There was a problem with the fetch operation: ' + e.message);
            });
    });


});

