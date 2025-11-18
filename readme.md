# Piper TTS Command-Line Utility

A command-line Python script to generate high-quality speech from text using the Piper TTS engine.

[![Version](https://img.shields.io/badge/version-v1.46.2-blue)](https://github.com/voothi/202412060110-piper-tts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This utility provides a simple, configurable interface to synthesize speech for multiple languages and can be used as a standalone tool or as a backend for other applications. All paths and model settings are managed in a central `config.ini` file for easy customization.

## Table of Contents

- [Piper TTS Command-Line Utility](#piper-tts-command-line-utility)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation and Setup](#installation-and-setup)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Integrations](#integrations)
    - [Anki Add-on Backend](#anki-add-on-backend)
    - [System-Wide Hotkeys with AutoHotkey (AHKv2)](#system-wide-hotkeys-with-autohotkey-ahkv2)
  - [License](#license)

## Features

-   **Configuration-Driven**: All paths and settings are managed in an easy-to-edit `config.ini` file.
-   **Portable**: Relative paths allow the entire project folder to be moved without breaking.
-   **Extensible**: Add new languages and voices by simply updating the configuration file.
-   **Flexible Input**: Synthesize text provided directly as an argument or from the system clipboard.
-   **File Output**: Save the generated audio to a specified file path.
-   **Standalone Playback**: Instantly play back the generated audio for quick tests.

[Back to Top](#table-of-contents)

## Prerequisites

1.  **Windows 11**: These instructions are tailored for Windows 11.
2.  **Python 3**: Python 3 must be installed on your system.
3.  **FFplay (Optional)**: For direct audio playback, `ffplay.exe` (part of FFmpeg) should be available on your system.

## Installation and Setup

**Step 1: Clone this Repository**
```bash
git clone https://github.com/voothi/202412060110-piper-tts.git
cd 202412060110-piper-tts
```

**Step 2: Download Piper Engine and Voices**

Go to the [**Releases Page**](https://github.com/voothi/20241206010110-piper-tts/releases) and download the following two files:
-   `piper-windows-amd64.zip`
-   `piper-voices-de-en-ru.zip`

**Step 3: Unzip and Organize Files**

You must place the contents of the archives into specific folders inside the cloned repository directory.

1.  Inside the `202412060110-piper-tts` folder, create a new folder named `piper`.
2.  Extract the **contents** of `piper-windows-amd64.zip` directly into this new `piper` folder.
3.  Back in the main project folder, create another new folder named `piper-voices`.
4.  Extract the **contents** of `piper-voices-de-en-ru.zip` into the `piper-voices` folder.

Your final folder structure should look like this:
```
202412060110-piper-tts/
├── piper/
│   ├── piper.exe
│   └── ... (other required files)
├── piper-voices/
│   ├── de/
│   ├── en/
│   └── ru/
├── config.ini
├── config.ini.template
├── piper_tts.py
└── README.md
```

**Step 4: Configure the Script**

1.  Find the file `config.ini.template` in the project directory.
2.  **Make a copy** of this file and rename the copy to `config.ini`.
3.  Open `config.ini` and edit the paths to match your system. See the [Configuration](#configuration) section below for details.

**Step 5: Install Python Dependencies**
```bash
pip install pyperclip
```

**Step 6: Test the Installation**

Run a test command. The `--lang` argument is now optional and will use the default from your config file.
```bash
python piper_tts.py --text "Hello, world."
```
You should hear the synthesized audio.

[Back to Top](#table-of-contents)

## Configuration

All script settings are managed in `config.ini`. The most important setting to check is `ffplay_executable`.

-   **`[paths]` section**:
    -   `piper_executable`: Path to `piper.exe` relative to the project root. The default should be correct if you followed the setup guide.
    -   `voices_directory`: Path to the `piper-voices` folder. The default should be correct.
    -   `ffplay_executable`: **You must provide the full, absolute path to `ffplay.exe` on your system for audio playback to work.** If you don't need playback, you can leave this empty.
-   **`[tts_settings]` section**:
    -   `supported_languages`: A comma-separated list of language codes you want to use.
    -   `default_lang`: The language to use if you don't specify one with the `--lang` flag.
-   **`[voice_*]` sections**:
    -   Each section defines the model and config files for a specific language. To add a new voice, add it to `supported_languages` and create a corresponding `[voice_...]` section.

[Back to Top](#table-of-contents)

## Usage

| Argument          | Description                                                              | Required |
| ----------------- | ------------------------------------------------------------------------ | :------: |
| `--lang`          | Language code. If omitted, uses the default from `config.ini`.           |    No    |
| `--text`          | The text string to synthesize.                                           |    No    |
| `--clipboard`     | If present, use the text currently in the system clipboard as input.     |    No    |
| `--output-file`   | Full path to save the output `.wav` file. Disables auto-playback.        |    No    |
| `--speaker`       | The speaker ID to use (default is `0`).                                  |    No    |

*Note: You must provide either `--text` or `--clipboard`.*

**Example Commands:**

```bash
# Synthesize German text and play it back
python piper_tts.py --lang de --text "Hallo, wie geht es Ihnen?"

# Use the default language (e.g., 'en') with text from the clipboard
python piper_tts.py --clipboard

# Synthesize English text and save it to a file (no playback)
python piper_tts.py --lang en --text "This is a test." --output-file "C:\temp\test_audio.wav"
```

[Back to Top](#table-of-contents)

## Integrations

### Anki Add-on Backend

This script serves as the official backend for the [**gTTS Player with Piper Fallback for Anki**](https://github.com/voothi/20250421115831-anki-gtts-player) add-on.

### System-Wide Hotkeys with AutoHotkey (AHKv2)

Beyond Anki, this script can be integrated into your desktop environment to provide system-wide text-to-speech functionality. By using the provided AutoHotkey v2 scripts, you can select text in any application and have it read aloud with a keyboard shortcut.

-   [**tts.ahk**](https://github.com/voothi/20240411110510-autohotkey?tab=readme-ov-file#ttsahk): A script that triggers `piper_tts.py` to read the currently selected text using different hotkeys for each language (e.g., English, German, Russian).
-   [**kill-ffplay.ahk**](https://github.com/voothi/20240411110510-autohotkey?tab=readme-ov-file#kill-ffplayahk): A utility hotkey to immediately terminate the audio playback, useful for stopping long sentences.

[Back to Top](#table-of-contents)

## License

[MIT](./LICENSE)

[Back to Top](#table-of-contents)