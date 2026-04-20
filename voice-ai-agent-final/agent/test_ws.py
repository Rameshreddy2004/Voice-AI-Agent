import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as ws:
        await ws.send(b"book appointment tomorrow with cardiologist")
        response = await ws.recv()
        print("Response:", response)

asyncio.run(test())