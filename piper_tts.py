import subprocess
import argparse
import pyperclip
from datetime import datetime
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def to_lower_case(input_string):
    # Remove HTML tags and other hidden characters
    cleaned_string = re.sub(r'<[^<]+?>', '', input_string)
    cleaned_string = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_string)
    # Replace new lines with spaces, except when a new line follows a space
    cleaned_string = re.sub(r'\n(?!\s)', ' ', cleaned_string)
    return cleaned_string.lower()

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Text-to-Speech using Piper TTS')
    parser.add_argument('--lang', type=str, required=True, help='Language code (e.g., "en" for English, "de" for German, "ru" for Russian)')
    parser.add_argument('--speaker', type=int, default=0, help='Speaker ID (default is 0)')
    parser.add_argument('--text', type=str, help='Text to synthesize')
    parser.add_argument('--clipboard', action='store_true', help='Read text from clipboard and copy synthesized text to the clipboard')
    parser.add_argument('--save-only', action='store_true', help='Save audio output without playback')

    args = parser.parse_args()
    
    # Determine the text to synthesize
    if args.clipboard:
        clipboard_text = get_clipboard_text()
        if not clipboard_text:
            parser.error('Clipboard is empty')
        text_to_synthesize = to_lower_case(clipboard_text)
    else:
        if args.text is None:
            parser.error('The --text argument must be provided if --clipboard is not used')
        text_to_synthesize = args.text
    
    # Define model paths based on the --lang argument (assuming a default model for each language)
    if args.lang == 'en':
        piper_path = r'U:/voothi/20241206010110-piper-tts/piper/piper.exe'
        model_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/en/en_US/ljspeech/high/en_US-ljspeech-high.onnx'
        config_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/en/en_US/ljspeech/high/en_US-ljspeech-high.onnx.json'
    elif args.lang == 'de':
        piper_path = r'U:/voothi/20241206010110-piper-tts/piper/piper.exe'
        model_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx'
        config_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx.json'
    elif args.lang == 'ru':
        piper_path = r'U:/voothi/20241206010110-piper-tts/piper/piper.exe'
        model_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/ru/ru_RU/irina/medium/ru_RU-irina-medium.onnx'
        config_path = r'U:/voothi/20241206010110-piper-tts/piper-voices/ru/ru_RU/irina/medium/ru_RU-irina-medium.onnx.json'
    else:
        print(f"Unsupported language: {args.lang}. Please use 'en', 'de', or 'ru'.")
        return
    
    # Determine output file path
    if args.save_only:
        # Generate timestamp in the format YYYYMMDDHHMMSS for output file
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_file = f'C:/Tools/piper-tts/{timestamp}-output.wav'
        print(f"Audio will be saved to: {output_file}")
    else:
        output_file = r'U:/voothi/20241206010110-piper-tts/output.wav'
    
    # Create the command to run the Piper TTS with the --speaker option
    command = [
        piper_path,
        '--model', model_path,
        '--config', config_path,
        '--output_file', output_file,
        '--speaker', str(args.speaker)
    ]
    
    # Synthesize the speech
    print(f'Synthesizing text: "{text_to_synthesize}"')
    
    # Call Piper TTS
    subprocess.run(command, input=text_to_synthesize, text=True)
    
    if not args.save_only:
        # Play the output audio using ffplay only if save_only is not used
        ffplay_path = r'C:/Tools/ffmpeg/ffmpeg-7.1-essentials_build/bin/ffplay.exe'
        play_command = [ffplay_path, '-nodisp', '-autoexit', output_file]
        print(f'Playing audio: {output_file}')
        subprocess.run(play_command)
    
    # Copy the synthesized text to the clipboard if --clipboard is specified
    if args.clipboard:
        set_clipboard_text(text_to_synthesize)
        print(f"Copied text to clipboard: \"{text_to_synthesize}\"")

if __name__ == '__main__':
    main()