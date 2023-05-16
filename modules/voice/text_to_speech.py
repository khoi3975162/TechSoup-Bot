import json
import os

with open(os.path.dirname('./config.json')) as f:
    config = json.load(f)

model = None

if config['el_key'] != '':
    model = 'el'
    import elevenlabs
    elevenlabs.set_api_key(config['el_key'])
else:
    model = 'pyttsx3'
    import pyttsx3
    # initialize pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)


def pyttsx3_tts(text: str, filename: str):
    """
    The function `pyttsx3_tts` saves text as an audio file using the pyttsx3 library with a modified
    pitch.

    :param text: The text that you want to convert to speech and save as an audio file
    :type text: str
    :param filename: The filename parameter is a string that represents the name of the file where the
    text-to-speech output will be saved
    :type filename: str
    """
    say = f'<pitch middle="8">{text}</pitch>'  # higher pitch
    engine.save_to_file(say, filename)
    engine.runAndWait()


def el_tts(text: str, filename: str):
    """
    The function `el_tts` generates an audio file from a given text using the text-to-speech service
    provided by Eleven Labs, and saves it with the specified filename.

    :param text: The text that needs to be converted to speech
    :type text: str
    :param filename: The filename parameter is a string that represents the name of the file where the
    generated audio will be saved
    :type filename: str
    """
    voice = "Bella"
    audio = elevenlabs.generate(text, voice=voice)
    elevenlabs.save(audio, filename)


if model == 'el':
    tts = el_tts
else:
    tts = pyttsx3_tts
