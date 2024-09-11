# Desktop Assistant - "Tiger"

## Overview

**Tiger** is a voice-controlled desktop assistant developed using Python. The assistant performs various tasks based on voice commands, such as opening websites, playing music, fetching information from Wikipedia, sending emails, and more.

## Features

- **Voice Recognition**: Uses Google Speech Recognition to recognize user commands.
- **Text-to-Speech**: Converts text responses to voice using pyttsx3.
- **Wikipedia Integration**: Searches and reads out summaries from Wikipedia.
- **Time Announcement**: Provides the current time on command.
- **File and App Management**: Can open applications like Notepad++, Spotify, Dev-C++, and browsers like Google Chrome, Edge, and Firefox.
- **Music Playback**: Automatically plays music from a predefined folder.
- **Email Sending**: Allows sending emails through voice commands.
  
## How It Works

1. **Voice Command Input**: Using the `speech_recognition` library, Tiger listens to the user's commands via the microphone.
2. **Task Execution**: Depending on the command, it executes different tasks like opening apps, fetching Wikipedia info, telling the time, etc.
3. **Response**: After executing the command, Tiger responds by speaking the result using the `pyttsx3` text-to-speech engine.

## Prerequisites

Before you run the project, make sure you have the following libraries installed:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pyaudio
```

## Setup and Execution

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/desktop-assistant-tiger.git
   ```
   
2. Install the required Python libraries (mentioned in Prerequisites).

3. Run the `main.py` file to start the assistant:
   ```bash
   python main.py
   ```

4. Tiger will greet you and be ready to accept your commands.

## Available Commands

- **"Wikipedia"**: Searches Wikipedia and reads out a summary.
- **"Open YouTube"**: Opens YouTube in the default web browser.
- **"Play Music"**: Plays music from a specified directory.
- **"Open [App Name]"**: Opens applications like Notepad++, Spotify, Dev-C++, Google Chrome, etc.
- **"Send Email to Harry"**: Sends an email after asking for the content of the email.
- **"What's the time?"**: Speaks the current time.
- **"Quit" or "Exit"**: Closes the assistant.

## Modifying the Project

You can easily customize the assistant by adding more commands to the `if-elif` blocks in the `main.py` file. For instance, you can include additional applications to open, integrate new web services, or handle more complex tasks.

## Notes

- Ensure your microphone is working correctly, as Tiger relies on it to listen to commands.
- If using email functionality, replace `youremail@gmail.com` and `your-password` with valid credentials or use environment variables for better security.

## Author

**Prateek Kumawat**  
Email: [kumawatprateek008@gmail.com](mailto:kumawatprateek008@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
