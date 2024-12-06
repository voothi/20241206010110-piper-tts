import subprocess
import argparse

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Text-to-Speech using Piper TTS')
    parser.add_argument('--lang', type=str, required=True, help='Language code (e.g., "en")')
    parser.add_argument('--text', type=str, required=True, help='Text to synthesize')
    args = parser.parse_args()

    # Define paths directly
    piper_path = r'C:\Tools\piper-tts\piper\piper.exe'  # Adjust the path as necessary
    model_path = r'C:\Tools\piper-tts\piper-voices\en\en_US\ljspeech\high\en_US-ljspeech-high.onnx'
    config_path = r'C:\Tools\piper-tts\piper-voices\en\en_US\ljspeech\high\en_en_US_ljspeech_high_en_US-ljspeech-high.onnx.json'
    output_file = 'output.wav'

    # Create the command to run the Piper TTS
    command = [
        piper_path,
        '--model', model_path,
        '--config', config_path,
        '--output_file', output_file
    ]

    # Synthesize the speech
    print(f'Synthesizing text: "{args.text}"')
    
    # Call Piper TTS
    subprocess.run(command, input=args.text, text=True)

    # Play the output audio using ffplay
    ffplay_path = r'C:\Tools\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffplay.exe'
    play_command = [ffplay_path, '-nodisp', '-autoexit', output_file]

    print(f'Playing audio: {output_file}')
    subprocess.run(play_command)

if __name__ == '__main__':
    main()