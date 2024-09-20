from openai import OpenAI
from pathlib import Path
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from google.cloud import translate_v2 as translate

#https://platform.openai.com/docs/guides/text-to-speech/quickstart
#api_key = ""
client = OpenAI(api_key=api_key)

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

#https://platform.openai.com/docs/guides/speech-to-text
#https://platform.openai.com/docs/api-reference/audio/createSpeech
# Speech-to-Text (STT) using OpenAI's Whisper model
def speech_to_text(file_name):
    audio_file= open(file_name, "rb") # input formats can be "mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        #response_format="text" # can be "json", "text", "srt", "verbose_json", "vtt"
    )
    return transcription.text

print(speech_to_text("audio.mp3"))

# Google Cloud Translation
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

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result

translate_text("zh", "Hi, how are you?")

# translate supported languages into English
""" Languages supported: Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, 
Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, 
Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, 
Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh."""
audio_file = open(speech_file_path, "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file,
  prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8" # prompt is used to recognise words that are misunderstood so that model can recognise the words when they hear it 
)
print(translation.text)

# Fixing errors in prompt using GPT 4 for post processing
system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

def generate_corrected_transcript(temperature, system_prompt, audio_file):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    return completion.choices[0].message.content

corrected_text = generate_corrected_transcript(0, system_prompt, speech_file_path)


"""
# Initialize recognizer
recognizer = sr.Recognizer()

# make a function to get result from user input and translate to desired language
def get_user_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google's STT API
            user_text = recognizer.recognize_google(audio)
            print(f"User said: {user_text}")
            return user_text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def text_to_speech(text):
    response = openai.Audio.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    # Save and play the response
    speech_file = "response.mp3"
    with open(speech_file, "wb") as file:
        for chunk in response.with_streaming_response():
            file.write(chunk)

    # Play the speech
    audio = AudioSegment.from_mp3(speech_file)
    play(audio)

# make a function to run conversation with code below:
while True:
    user_input = get_user_input()
    if user_input:
        response_text = generate_response(user_input)
        print(f"Assistant: {response_text}")
        text_to_speech(response_text)
"""