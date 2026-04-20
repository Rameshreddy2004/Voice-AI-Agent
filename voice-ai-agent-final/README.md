# Real-Time Multilingual Voice AI Agent

## Features
- WebSocket real-time voice pipeline
- OpenAI tool-calling
- Redis session memory
- Appointment scheduling engine
- Latency logging

## Run
1. Setup Redis
2. Add OPENAI_API_KEY
3. pip install -r requirements.txt
4. uvicorn backend.main:app --reload

## Architecture
Voice → STT → LLM → Tools → Scheduler → TTS

## Latency
Logged per request in console

## TODO (for full marks)
- Replace STT with Whisper
- Replace TTS with ElevenLabs
- Add PostgreSQL
- Add outbound calling
