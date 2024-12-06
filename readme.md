## tasks / ideas
[] creating a file with the string lowercase in the folder with the timestamp ZID (20241206020041)

[] deleting file at the beginning of script execution for speed and cache

[] transition from file to raw
Try the parameters after execution.
```
U:\voothi\voothi.root\voothi\20241205222658-piper-for-goldendict.md
```

[x] add russian lang

[] add a new argument --model to the utility call
The --model argument has a choice between numbers 0, 1, 2... Take out the choice of one of the commented models by number into the argument.
```
    elif args.lang == 'de':
        piper_path = r'C:\Tools\piper-tts\piper\piper.exe'
        # model_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\thorsten\high\de_DE-thorsten-high.onnx'
        # config_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\thorsten\high\de_DE-thorsten-high.onnx.json'
        model_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\pavoque\low\de_DE-pavoque-low.onnx'
        config_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\pavoque\low\de_DE-pavoque-low.onnx.json'
        # model_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\mls\medium\de_DE-mls-medium.onnx'
        # config_path = r'C:\Tools\piper-tts\piper-voices\de\de_DE\mls\medium\de_DE-mls-medium.onnx.json'
```

## tests / use
```
C:\Python\Python312\python.exe C:\Tools\piper-tts\piper_tts.py --lang en --text "Welcome to the world of speech synthesis!"
C:\Python\Python312\python.exe C:\Tools\piper-tts\piper_tts.py --lang de --text "Willkommen in der Welt der Sprachsynthese!"
C:\Python\Python312\python.exe C:\Tools\piper-tts\piper_tts.py --lang ru --text "Добро пожаловать в мир синтеза речи!"
```

## models
de_DE-thorsten-high.onnx  
very fast  

de_DE-mls-medium.onnx  
does not work on multi-word phrases  

likes voices --speaker 8,16,18,20,21,22,24,25,27,32  
I didn't look further. There are 236 of them. See the file de_DE-mls-medium.onnx.json.  
