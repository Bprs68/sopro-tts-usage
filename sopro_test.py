from sopro import SoproTTS

tts = SoproTTS.from_pretrained("samuel-vitorino/sopro", device="cpu")

wav = tts.synthesize(
    "The world is a beautiful place. Strangers help people all the time.",
    ref_audio_path="p314_005.wav"
)

tts.save_wav(r"generated_audio\out.wav", wav)