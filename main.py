from openai import OpenAI
from pathlib import Path
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech as tts

openAI_api_key = ""

client = OpenAI(api_key=openAI_api_key)

# Text-to-Speech (TTS) using OpenAI 
def text_to_speech(file_name):
    user_input = input("Enter some text: ")
    print(user_input, "was entered.")
    # file path for the speech file
    speech_file_path = Path(__file__).parent / file_name
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy", # Other voices for tts are "Echo", "Fable", "Onyx", "Nova", "Shimmer"
    input=user_input
    )
    return response.stream_to_file(speech_file_path) # output formats can be "mp3", "opus", "aac", "flac", "pcm"

text_to_speech("audio.mp3")

"""
Opus: For internet streaming and communication, low latency.
AAC: For digital audio compression, preferred by YouTube, Android, iOS.
FLAC: For lossless audio compression, favored by audio enthusiasts for archiving.
WAV: Uncompressed WAV audio, suitable for low-latency applications to avoid decoding overhead.
PCM: Similar to WAV but containing the raw samples in 24kHz (16-bit signed, low-endian), without the header.
"""
# Speech-to-Text (STT) using OpenAI's Whisper model
def speech_to_text(file_name):
    audio_file= open(file_name, "rb") # input formats can be "mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        #response_format="text" # can be "json", "text", "srt", "verbose_json", "vtt"
    )
    return transcription.text

text_to_translate = speech_to_text("audio.mp3")
print(text_to_translate)

# Google Cloud Translation API to translate languages
def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://cloud.google.com/translate/docs/languages
    """

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text user entered: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result

translated_text = translate_text("zh", text_to_translate).get('translatedText') 
print(translated_text)

# Text-to-Speech using Goolge Cloud Text to Speech API
def gcloud_tts(text_to_be_translated, lang_code):

    # Instantiates a client
    client = tts.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = tts.SynthesisInput(text=text_to_be_translated)

    # Build voice request
    voice = tts.VoiceSelectionParams(
        language_code=lang_code, 
        ssml_gender=tts.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # output audio file
    with open("translated_audio.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "translated_audio.mp3"')

gcloud_tts(translated_text, "zh-CN")