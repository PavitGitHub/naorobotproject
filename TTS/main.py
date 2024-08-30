from openai import OpenAI
from pathlib import Path
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

#https://platform.openai.com/docs/guides/text-to-speech/quickstart
apiKey = "get it from openai account"

client = OpenAI(api_key=apiKey)
# Initialize recognizer
recognizer = sr.Recognizer()

speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)

#https://platform.openai.com/docs/guides/speech-to-text
audio_file= open("speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

"""
# translate supported languages into English
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)
"""

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
