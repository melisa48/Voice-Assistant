# Voice Assistant
- This project implements a voice assistant application using Python, integrating with Wolfram Alpha for query responses and
providing text-to-speech functionality using pyttsx3.
- The application utilizes PySimpleGUI for the graphical user interface.

## Features
- Voice Commands: Users can input commands via voice or text input.
- Query Processing: Queries are processed using Wolfram Alpha's API for factual responses.
- Text-to-Speech: Responses are converted to speech using pyttsx3 for auditory feedback.
- User Interface: Simple GUI built with PySimpleGUI for ease of interaction.
## Technologies Used
- Python
- Wolfram Alpha API
- pyttsx3
- PySimpleGUI

## Installation
1. Clone the repository:
- git clone https://github.com/your-username/voice-assistant.git
- cd voice-assistant
2. Install dependencies:
- pip install -r requirements.txt
- Ensure you have Python installed and configured.

3. Obtain API Keys:
- Wolfram Alpha: Sign up for an API key at Wolfram Alpha Developer Portal.
4. Update Configuration:
- Replace "YOUR_WOLFRAM_ALPHA_API_KEY" in voice-assistant.py with your actual Wolfram Alpha API key.

## Usage
1. Run the application:
- python voice-assistant.py
- Enter commands via the GUI input field or speak directly to the voice assistant.
Examples
- Input: "hello"
- Output: "Greetings! How can I assist you today?"
- Input: "how are you?"
- Output: "I am doing well, thank you."
- Input: "can you help me to write email?"
- Output: "No relevant information found."

## Known Issues
- Limited natural language understanding; commands must be specific and structured.
## Contributing
- Contributions are welcome! Please fork the repository and submit pull requests.
