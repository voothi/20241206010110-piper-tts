# Piper TTS Command-Line Utility

A command-line Python script to generate high-quality speech from text using the Piper TTS engine.

[![Version](https://img.shields.io/badge/version-v1.1-blue)](https://github.com/voothi/20241206010110-piper-tts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This utility provides a simple interface to synthesize speech for multiple languages (English, German, Russian) and can be used as a standalone tool or as a backend for other applications, such as the [gTTS Player with Piper Fallback for Anki](https://github.com/voothi/20250421115831-anki-gtts-player).

## Table of Contents

- [Piper TTS Command-Line Utility](#piper-tts-command-line-utility)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
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

1.  **Python 3**: Python 3 must be installed on your system.
2.  **Piper TTS Engine**: The repository includes the Piper executable and voice models. No separate download of Piper is needed.
3.  **FFplay (Optional)**: For direct audio playback, `ffplay.exe` (part of FFmpeg) should be available on your system.

## Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/voothi/20241206010110-piper-tts.git
    ```
2.  Navigate to the repository folder:
    ```bash
    cd 20241206010110-piper-tts
    ```
3.  Install the required Python library:
    ```bash
    pip install pyperclip
    ```
4.  Test the script from your terminal. Ensure the paths inside `piper_tts.py` are correct for your system if you move the folders.

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

# Synthesize Russian text from the clipboard and play it back
python piper_tts.py --lang ru --clipboard

# Synthesize English text and save it to a specific file for Anki (no playback)
python piper_tts.py --lang en --text "This is a test." --output-file "C:\Users\user\Desktop\anki_audio.wav"
```

[Back to Top](#table-of-contents)

## Integration

This script is the official backend for the [**gTTS Player with Piper Fallback for Anki**](https://github.com/voothi/20250421115831-anki-gtts-player) add-on. The add-on calls this utility with the `--output-file` argument to generate audio when an internet connection is not available.

[Back to Top](#table-of-contents)

## License

[MIT](./LICENSE)

[Back to Top](#table-of-contents)