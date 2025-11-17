# Piper TTS Command-Line Utility

A command-line Python script to generate high-quality speech from text using the Piper TTS engine.

[![Version](https://img.shields.io/badge/version-v1.1-blue)](https://github.com/voothi/202412060110-piper-tts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This utility provides a simple interface to synthesize speech for multiple languages (English, German, Russian) and can be used as a standalone tool or as a backend for other applications, such as the [gTTS Player with Piper Fallback for Anki](https://github.com/voothi/20250421115831-anki-gtts-player).

## Table of Contents

- [Piper TTS Command-Line Utility](#piper-tts-command-line-utility)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation and Setup](#installation-and-setup)
  - [Usage](#usage)
  - [Integration](#integration)
  - [License](#license)

## Features

-   **Multi-Language Support**: Pre-configured for English, German, and Russian voices.
-   **Flexible Input**: Synthesize text provided directly as an argument or from the system clipboard.
-   **File Output**: Save the generated audio to a specified file path, ideal for integration with other scripts.
-   **Standalone Playback**: Instantly play back the generated audio for quick tests.

[Back to Top](#table-of-contents)

## Prerequisites

1.  **Windows 11**: These instructions are tailored for Windows 11.
2.  **Python 3**: Python 3 must be installed on your system.
3.  **FFplay (Optional)**: For direct audio playback, `ffplay.exe` (part of FFmpeg) should be available on your system and ideally in your system's PATH.

## Installation and Setup

The setup involves cloning the script repository and then downloading and placing the Piper engine and voice models into the correct folders.

**Step 1: Clone this Repository**
```bash
git clone https://github.com/voothi/202412060110-piper-tts.git
cd 202412060110-piper-tts
```

**Step 2: Download Piper Engine and Voices**

Go to the [**Releases Page**](https://github.com/voothi/202412060110-piper-tts/releases) and download the following files:
-   `piper-windows-amd64.zip`
-   `piper-voices-en.zip`
-   `piper-voices-de.zip`
-   `piper-voices-ru.zip`

**Step 3: Unzip and Organize Files**

You must place the contents of the archives into specific folders inside the cloned repository directory. The final structure must look like the one below.

1.  Inside the `202412060110-piper-tts` folder, create a new folder named `piper`.
2.  Extract the **contents** of `piper-windows-amd64.zip` directly into this new `piper` folder.
3.  Back in the main project folder, create another new folder named `piper-voices`.
4.  Extract the **contents** of `piper-voices-de-en-ru.zip` (which are the `de`, `en`, and `ru` folders) into the `piper-voices` folder.

Your final folder structure should look like this:
```
202412060110-piper-tts/
├── piper/
│   ├── piper.exe
│   ├── onnxruntime.dll
│   └── ... (other required files)
├── piper-voices/
│   ├── de/
│   ├── en/
│   └── ru/
├── piper_tts.py
└── README.md
```

**Step 4: Install Python Dependencies**

Open a terminal in the project directory and run:
```bash
pip install pyperclip```

**Step 5: Test the Installation**

Run a test command to ensure everything is working correctly:
```bash
python piper_tts.py --lang en --text "Hello, world."
```
You should hear the synthesized audio.

[Back to Top](#table-of-contents)

## Usage

The script is controlled via command-line arguments.

| Argument          | Description                                                              | Required |
| ----------------- | ------------------------------------------------------------------------ | :------: |
| `--lang`          | Language code: `en`, `de`, or `ru`.                                      |   Yes    |
| `--text`          | The text string to synthesize.                                           |    No    |
| `--clipboard`     | If present, use the text currently in the system clipboard as input.     |    No    |
| `--output-file`   | Full path to save the output `.wav` file. Disables auto-playback.        |    No    |
| `--speaker`       | The speaker ID to use (default is `0`).                                  |    No    |

**Example Commands:**

```bash
# Synthesize German text and play it back immediately
python piper_tts.py --lang de --text "Hallo, wie geht es Ihnen?"

# Synthesize English text and save it to a specific file (no playback)
python piper_tts.py --lang en --text "This is a test." --output-file "C:\temp\test_audio.wav"
```

[Back to Top](#table-of-contents)

## Integration

This script is the official backend for the [**gTTS Player with Piper Fallback for Anki**](https://github.com/voothi/20250421115831-anki-gtts-player) add-on. The add-on calls this utility with the `--output-file` argument to generate audio when an internet connection is not available.

[Back to Top](#table-of-contents)

## License

[MIT](./LICENSE)

[Back to Top](#table-of-contents)