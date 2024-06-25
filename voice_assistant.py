import wolframalpha
import pyttsx3
import PySimpleGUI as sg
import nltk
from nltk.tokenize import word_tokenize

# Initialize NLTK
nltk.download('punkt')

# Initialize Wolfram Alpha client
client = wolframalpha.Client("YOUR_WOLFRAM_ALPHA_API_KEY")

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# PySimpleGUI setup
sg.theme('BrownBlue')
layout = [
    [sg.Text('Enter a Command '), sg.InputText(key='-INPUT-')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Output(size=(60, 10))]  # Add an output element for displaying messages
]
window = sg.Window('Voice Assistant', layout)

previous_command = None  # Variable to store previous command for contextual awareness

def process_command(command):
    global previous_command
    tokens = word_tokenize(command.lower())
    
    # Check if command is related to the previous command
    if previous_command is not None:
        if 'how' in tokens and 'you' in tokens:
            response = "I am doing well, thank you."
        else:
            try:
                # Query Wolfram Alpha
                res = client.query(command)
                if res.results:
                    response = next(res.results).text
                else:
                    response = "No relevant information found."
            except Exception as e:
                response = f"Error: {str(e)}"
    else:
        # Basic command recognition
        if 'hello' in tokens:
            response = "Greetings! How can I assist you today?"
        else:
            try:
                # Query Wolfram Alpha
                res = client.query(command)
                if res.results:
                    response = next(res.results).text
                else:
                    response = "No relevant information found."
            except Exception as e:
                response = f"Error: {str(e)}"

    previous_command = command  # Update previous_command to current command
    return response

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    command = values['-INPUT-'].strip()

    if command:
        # Process the command and get the response
        response = process_command(command)

        # Display response in the output element
        print(f"User Command: {command}")
        print(f"Assistant Response: {response}")

        # Speak the response
        engine.say(response)
        engine.runAndWait()

    else:
        # Handle empty command
        sg.popup('Please enter a command.', title='Error')

window.close()
