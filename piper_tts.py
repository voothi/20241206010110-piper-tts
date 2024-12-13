import subprocess
import argparse
from datetime import datetime

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Text-to-Speech using Piper TTS')
    parser.add_argument('--lang', type=str, required=True, help='Language code (e.g., "en" for English, "de" for German, "ru" for Russian)')
    parser.add_argument('--speaker', type=int, default=0, help='Speaker ID (default is 0)')
    parser.add_argument('--text', type=str, required=True, help='Text to synthesize')
    parser.add_argument('--save-only-to', type=str, help='Path to save audio output without playback')
    args = parser.parse_args()
    
    # Define paths based on language
    if args.lang == 'en':
        piper_path = r'C:\Tools\piper-tts\piper\piper.exe'
        model_path = r'C:\Tools\piper-tts\piper-voices\en\en_US\ljspeech\high\en_US-ljspeech-high.onnx'
        config_path = r'C:\Tools\piper-tts\piper-voices\en\en_US\ljspeech\high\en_US-ljspeech-high.onnx.json'
    elif args.lang == 'de':
        piper_path = r'C:\Tools\piper-tts\piper\piper.exe'
        model_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\pavoque\low\de_DE-pavoque-low.onnx'
        config_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\pavoque\low\de_DE-pavoque-low.onnx.json'
    elif args.lang == 'ru':
        piper_path = r'C:\Tools\piper-tts\piper\piper.exe'
        model_path = r'C:\Tools\piper-tts\piper-voices\ru\ru_RU\irina\medium\ru_RU-irina-medium.onnx'
        config_path = r'C:\Tools\piper-tts\piper-voices\ru\ru_RU\irina\medium\ru_RU-irina-medium.onnx.json'
    else:
        print(f"Unsupported language: {args.lang}. Please use 'en', 'de', or 'ru'.")
        return
    
    # Determine output file path
    if args.save_only_to:
        output_file = args.save_only_to
    else:
        # Generate timestamp in the format YYYYMMDDHHMMSS
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_file = f'C:\\Tools\\piper-tts\\{timestamp}-output.wav'
    
    # Create the command to run the Piper TTS with the --speaker option
    command = [
        piper_path,
        '--model', model_path,
        '--config', config_path,
        '--output_file', output_file,
        '--speaker', str(args.speaker)  # Use the speaker parameter from arguments
    ]
    
    # Synthesize the speech
    print(f'Synthesizing text: "{args.text}"')
    
    # Call Piper TTS
    subprocess.run(command, input=args.text, text=True)
    
    if not args.save_only_to:
        # Play the output audio using ffplay only if save_only_to is not used
        ffplay_path = r'C:\Tools\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffplay.exe'
        play_command = [ffplay_path, '-nodisp', '-autoexit', output_file]
        print(f'Playing audio: {output_file}')
        subprocess.run(play_command)

if __name__ == '__main__':
    main()