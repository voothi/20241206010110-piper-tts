import subprocess
import argparse
import pyperclip
import re
import sys
from pathlib import Path

def get_clipboard_text():
    """Gets text from the clipboard."""
    return pyperclip.paste()

def set_clipboard_text(text):
    """Sets text to the clipboard."""
    pyperclip.copy(text)

def sanitize_text(input_string):
    """Removes HTML tags, control characters, and normalizes line breaks."""
    # This function is kept simple for now, but can be expanded.
    cleaned_string = re.sub(r'<[^>]+?>', '', input_string)
    cleaned_string = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_string)
    cleaned_string = cleaned_string.replace('\n', ' ').strip()
    return cleaned_string

def main():
    """Main function to run Piper TTS."""
    parser = argparse.ArgumentParser(description='Text-to-Speech using Piper TTS')
    parser.add_argument('--lang', type=str, required=True, help='Language code (e.g., "en", "de", "ru")')
    parser.add_argument('--speaker', type=int, default=0, help='Speaker ID (default is 0)')
    parser.add_argument('--text', type=str, help='Text to synthesize')
    parser.add_argument('--clipboard', action='store_true', help='Read text from clipboard')
    
    # New argument for Anki integration.
    # It specifies the full path where the audio file should be saved.
    parser.add_argument('--output-file', type=str, help='Full path to save the output WAV file. If provided, playback is skipped.')

    args = parser.parse_args()
    
    # --- Determine the text to synthesize ---
    if args.text:
        text_to_synthesize = sanitize_text(args.text)
    elif args.clipboard:
        clipboard_text = get_clipboard_text()
        if not clipboard_text:
            print("Error: --clipboard flag was used, but the clipboard is empty.", file=sys.stderr)
            sys.exit(1)
        text_to_synthesize = sanitize_text(clipboard_text)
    else:
        parser.error('Either the --text or --clipboard argument must be provided.')

    # --- Define model paths ---
    base_path = Path("U:/voothi/20241206010110-piper-tts")
    piper_exe_path = base_path / "piper" / "piper.exe"
    
    model_paths = {
        'en': {
            'model': base_path / "piper-voices/en/en_US/ljspeech/high/en_US-ljspeech-high.onnx",
            'config': base_path / "piper-voices/en/en_US/ljspeech/high/en_US-ljspeech-high.onnx.json"
        },
        'de': {
            'model': base_path / "piper-voices/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx",
            'config': base_path / "piper-voices/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx.json"
        },
        'ru': {
            'model': base_path / "piper-voices/ru/ru_RU/irina/medium/ru_RU-irina-medium.onnx",
            'config': base_path / "piper-voices/ru/ru_RU/irina/medium/ru_RU-irina-medium.onnx.json"
        }
    }
    
    if args.lang not in model_paths:
        print(f"Error: Unsupported language '{args.lang}'. Supported languages are: {list(model_paths.keys())}", file=sys.stderr)
        sys.exit(1)

    selected_model = model_paths[args.lang]
    
    # --- Determine output file path ---
    # If --output-file is provided (by Anki), use it directly.
    # Otherwise, fall back to the default for standalone use.
    output_file = args.output_file if args.output_file else str(base_path / "output.wav")
    
    # --- Build and run the Piper command ---
    command = [
        str(piper_exe_path),
        '--model', str(selected_model['model']),
        '--config', str(selected_model['config']),
        '--output_file', output_file,
        '--speaker', str(args.speaker)
    ]
    
    print(f'Piper TTS: Synthesizing "{text_to_synthesize}"...')
    
    try:
        # We use subprocess.run to execute the command.
        # The text is passed via standard input (stdin).
        # We capture the output to check for errors.
        process = subprocess.run(
            command, 
            input=text_to_synthesize, 
            text=True, 
            encoding='utf-8', 
            capture_output=True,
            check=True  # This will raise CalledProcessError if the return code is non-zero
        )
    except FileNotFoundError:
        print(f"Error: Could not find piper.exe at '{piper_exe_path}'. Please check the path.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("Error: Piper process failed.", file=sys.stderr)
        print(f"Return Code: {e.returncode}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)
        
    print(f'Successfully created audio file at: {output_file}')

    # --- Play audio only if NOT called for Anki (i.e., --output-file is not set) ---
    if not args.output_file:
        ffplay_path = r'C:/Tools/ffmpeg/ffmpeg-7.1-essentials_build/bin/ffplay.exe'
        play_command = [ffplay_path, '-nodisp', '-autoexit', output_file]
        print(f'Playing audio: {output_file}')
        subprocess.run(play_command, capture_output=True)

if __name__ == '__main__':
    main()