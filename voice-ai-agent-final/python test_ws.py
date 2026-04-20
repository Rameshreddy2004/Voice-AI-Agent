import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8001/ws"
    async with websockets.connect(uri) as ws:
        await ws.send(b"hello doctor")
        response = await ws.recv()

        print("RAW RESPONSE:", response)
        print("DECODED:", response.decode())

asyncio.run(test())