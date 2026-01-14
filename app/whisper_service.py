from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu")

def transcribe_audio(audio_path: str) -> str:
    segments, _ = model.transcribe(audio_path)
    transcript = " ".join([seg.text for seg in segments])
    return transcript.strip()
