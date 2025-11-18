// piper_tts.py
import subprocess
import argparse
import pyperclip
import re
import sys
import configparser
from pathlib import Path

# --- Constants ---
PROJECT_ROOT = Path(__file__).resolve().parent
CONFIG_FILE = PROJECT_ROOT / "config.ini"

def load_configuration(config_path):
    """Loads configuration from the INI file."""
    if not config_path.exists():
        print(f"Error: Configuration file not found at '{config_path}'.", file=sys.stderr)
        print("Please copy 'config.ini.template' to 'config.ini' and configure it.", file=sys.stderr)
        sys.exit(1)
    
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def load_models_from_config(config, project_root):
    """Dynamically builds the model paths dictionary from the config object."""
    model_paths = {}
    try:
        supported_langs = [lang.strip() for lang in config.get('tts_settings', 'supported_languages').split(',')]
        voices_dir = project_root / config.get('paths', 'voices_directory')

        for lang in supported_langs:
            section_name = f'voice_{lang}'
            if config.has_section(section_name):
                model_paths[lang] = {
                    'model': voices_dir / config.get(section_name, 'model'),
                    'config': voices_dir / config.get(section_name, 'config')
                }
            else:
                print(f"Warning: Language '{lang}' is listed in supported_languages but section '[{section_name}]' is missing in config.", file=sys.stderr)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Error: Missing configuration in '{CONFIG_FILE}': {e}", file=sys.stderr)
        sys.exit(1)
        
    return model_paths

def get_clipboard_text():
    """Gets text from the clipboard."""
    return pyperclip.paste()

def sanitize_text(input_string):
    """Removes HTML tags, control characters, and normalizes line breaks."""
    cleaned_string = re.sub(r'<[^>]+?>', '', input_string)
    cleaned_string = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_string)
    cleaned_string = cleaned_string.replace('\n', ' ').strip()
    return cleaned_string

def main():
    """Main function to run Piper TTS."""
    config = load_configuration(CONFIG_FILE)
    model_paths = load_models_from_config(config, PROJECT_ROOT)
    
    default_lang = config.get('tts_settings', 'default_lang', fallback='en')
    
    parser = argparse.ArgumentParser(description='Text-to-Speech using Piper TTS')
    parser.add_argument('--lang', type=str, default=default_lang, help=f'Language code (e.g., "en", "de"). Supported: {list(model_paths.keys())}. Default: {default_lang}')
    parser.add_argument('--speaker', type=int, default=0, help='Speaker ID (default is 0)')
    parser.add_argument('--text', type=str, help='Text to synthesize')
    parser.add_argument('--clipboard', action='store_true', help='Read text from clipboard')
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

    # --- Validate language and get model paths ---
    if args.lang not in model_paths:
        print(f"Error: Unsupported language '{args.lang}'. Supported languages are defined in config.ini: {list(model_paths.keys())}", file=sys.stderr)
        sys.exit(1)
    
    selected_model = model_paths[args.lang]
    
    # --- Get paths from config ---
    piper_exe_path = PROJECT_ROOT / config.get('paths', 'piper_executable')
    default_output_filename = config.get('paths', 'default_output_filename')
    
    # --- Determine output file path ---
    output_file = args.output_file if args.output_file else str(PROJECT_ROOT / default_output_filename)
    
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
        process = subprocess.run(
            command, 
            input=text_to_synthesize, 
            text=True, 
            encoding='utf-8', 
            capture_output=True,
            check=True
        )
    except FileNotFoundError:
        print(f"Error: Could not find piper.exe at '{piper_exe_path}'. Please check the 'piper_executable' path in config.ini.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("Error: Piper process failed.", file=sys.stderr)
        print(f"Return Code: {e.returncode}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)
        
    print(f'Successfully created audio file at: {output_file}')

    # --- Play audio only if not saving to a specific output file ---
    if not args.output_file:
        ffplay_path = config.get('paths', 'ffplay_executable', fallback='').strip()
        if ffplay_path:
            play_command = [ffplay_path, '-nodisp', '-autoexit', output_file]
            print(f'Playing audio: {output_file}')
            try:
                subprocess.run(play_command, capture_output=True, check=False)
            except FileNotFoundError:
                print(f"Warning: Could not find ffplay.exe at '{ffplay_path}'. Playback skipped.", file=sys.stderr)
                print("Please check the 'ffplay_executable' path in config.ini or leave it empty to disable playback.", file=sys.stderr)
        else:
            print("Playback skipped: 'ffplay_executable' is not set in config.ini.")


if __name__ == '__main__':
    main()