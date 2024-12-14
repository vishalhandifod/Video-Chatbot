import whisper
import os

def transcribe_audio(audio_path):
   
    model = whisper.load_model("base")
    

    result = model.transcribe(audio_path)
    
    transcription_text = result['text']
    
    return transcription_text
