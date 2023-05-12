import whisper
import torch
import numpy as np

model = whisper.load_model("base")


def stt_from_file(filename: str):
    """
    The function takes a filename as input and uses a speech-to-text model to transcribe the audio file
    into English text.

    :param filename: The name or path of the audio file that needs to be transcribed into text
    :type filename: str
    :return: the transcribed text from the audio file specified by the filename parameter using a
    speech-to-text model.
    """
    result = model.transcribe(filename, language='english')
    return result['text']
