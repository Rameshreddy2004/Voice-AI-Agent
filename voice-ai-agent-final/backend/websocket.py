from fastapi import APIRouter, WebSocket
from agent.orchestrator import process_audio

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    print("Client connected")

    try:
        while True:
            data = await ws.receive_bytes()
            print("Received:", data)

            response = await process_audio(data)

            await ws.send_bytes(response)

    except Exception as e:
        print("WebSocket error:", e)
        await ws.close()