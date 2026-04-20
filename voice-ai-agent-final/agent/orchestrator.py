import os
import time
from dotenv import load_dotenv
from openai import OpenAI

from services.stt import speech_to_text
from services.tts import text_to_speech

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def process_audio(audio_bytes: bytes):
    try:
        print("Received audio")

        # 1. Speech to Text
        text = await speech_to_text(audio_bytes)
        print("User said:", text)

        # 2. LLM (SAFE)
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful medical assistant."},
                    {"role": "user", "content": text}
                ]
            )

            reply = response.choices[0].message.content

            if not reply:
                reply = "Sorry, I couldn't understand."

        except Exception as e:
            print("LLM ERROR:", e)
            reply = "Hello! How can I help you?"

        print("Final reply:", reply)

        # 3. Text to Speech
        audio = await text_to_speech(reply)

        # Ensure bytes output
        if isinstance(audio, str):
            audio = audio.encode()

        return audio

    except Exception as e:
        print("SERVER ERROR:", e)
        return b"Error occurred"