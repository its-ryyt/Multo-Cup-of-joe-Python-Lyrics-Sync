# 🎵 Multo - Cup of Joe (Python Lyrics Sync)

A Python project that synchronizes the lyrics of "Multo" by Cup of Joe with audio playback, displaying the lyrics in real-time as the song plays.

## 📂 Project Overview

This application plays the song "Multo" and displays its lyrics in sync, enhancing the listening experience. It's a simple demonstration of handling timed events in Python.

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**

   Open your terminal or Git Bash and run:

   ```bash
   git clone https://github.com/its-ryyt/Multo-Cup-of-joe-Python-Lyrics-Sync.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd Multo-Cup-of-joe-Python-Lyrics-Sync
   ```

3. **Install required Python libraries**

   It's recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Then install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, you can install the necessary library directly:*

   ```bash
   pip install pillow
   pip install pip
   pip install playsound
   pip install pygame
   ```

   ![Installation Screenshot](https://github.com/user-attachments/assets/19983372-5fcb-408a-b888-41d682d4b969)

4. **Ensure the audio file is in place**

   Make sure the `Multo.mp3` file is located in the `mp3` directory within the project folder:

   ```
   Multo-Cup-of-joe-Python-Lyrics-Sync/
   ├── mp3/
   │   └── Multo.mp3
   └── multo_lyrics_sync.py
   ```

## 🎮 Usage

To run the application:

```bash
python multo_lyrics_sync.py
```

*Ensure that your terminal's current directory is the project folder.*

## 📝 Features

- Plays the song "Multo" by Cup of Joe.
- Displays lyrics in sync with the song playback.
- Simple and easy-to-understand code structure.

## 📸 Screenshots

*You can add screenshots or GIFs here to showcase the application's interface.*

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Cup of Joe](https://www.facebook.com/cupofjoemusic) for the inspiring song "Multo".
- [Playsound Library](https://pypi.org/project/playsound/) for audio playback functionality.
