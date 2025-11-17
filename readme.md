# Piper TTS Command-Line Utility

A simple and powerful command-line interface for the Piper TTS engine.

[![Version](https://img.shields.io/badge/version-v1.1-blue)](https://github.com/voothi/20241206010110-piper-tts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Python script acts as a wrapper around the `piper.exe` engine, allowing you to easily generate high-quality speech from text. It is designed for both standalone use and as a backend for other applications, most notably the [gTTS Player with Piper Fallback](https://github.com/voothi/20250421115831-anki-gtts-player) Anki add-on.

## Table of Contents

- [Piper TTS Command-Line Utility](#piper-tts-command-line-utility)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Command-Line Arguments](#command-line-arguments)
  - [Related Projects](#related-projects)
  - [License](#license)

## Features

-   Synthesize text to speech using local Piper models.
-   Support for multiple languages (easily configurable by adding models).
-   Accept text directly from a command-line argument or from the system clipboard.
-   Save generated audio to a specified `.wav` file path.
-   Includes optional standalone playback via `ffplay` for quick testing.

[Back to Top](#table-of-contents)

## Prerequisites

1.  **Python 3**: Must be installed on your system.
2.  **Piper TTS Engine**: You need the `piper.exe` executable and the required voice models (`.onnx` and `.json` files).
3.  **(Optional) FFmpeg**: For audio playback directly from the script, `ffplay.exe` (part of FFmpeg) should be in your system's PATH or located at the path specified in the script.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/voothi/20241206010110-piper-tts.git
    cd 20241206010110-piper-tts
    ```

2.  **Set up Piper Files**:
    -   Place the `piper.exe` executable inside the `piper` directory.
    -   Place your downloaded voice models inside the `piper-voices` directory, maintaining a structure like `piper-voices/<lang>/...`.

3.  **Install Python Dependencies**:
    ```bash
    pip install pyperclip
    ```

4.  **Test the Script**:
    Run a test command from your terminal to ensure everything is working.
    ```bash
    # Example for Windows
    C:\Python\Python312\python.exe piper_tts.py --lang en --text "Hello world"
    ```
    This should generate an `output.wav` file and play it if `ffplay` is available.

[Back to Top](#table-of-contents)

## Command-Line Arguments

The script is controlled via the following command-line arguments.

| Argument         | Description                                                                              | Required |
| ---------------- | ---------------------------------------------------------------------------------------- | :------: |
| `--lang`         | Two-letter language code (e.g., `en`, `de`, `ru`). Must match a configured model.          |   Yes    |
| `--speaker`      | The speaker ID for the selected model. Defaults to `0`.                                  |    No    |
| `--text`         | The string of text to synthesize.                                                        |    No*   |
| `--clipboard`    | If present, read text from the system clipboard instead of from `--text`.                |    No*   |
| `--output-file`  | Full path to save the output `.wav` file. If provided, audio playback is skipped.        |    No    |

_*One of `--text` or `--clipboard` must be provided._

[Back to Top](#table-of-contents)

## Related Projects

-   [**gTTS Player with Piper Fallback for Anki**](https://github.com/voothi/20250421115831-anki-gtts-player): This script is a core dependency for this Anki add-on, providing its essential offline TTS capabilities.

[Back to Top](#table-of-contents)

## License

[MIT](./LICENSE)

[Back to Top](#table-of-contents)