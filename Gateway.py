import asyncio
import websockets
import json
import random
from datetime import datetime

async def gate_handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        sensor_id = data.get("id_senzor")
        print(f"Received request for sensor ID: {sensor_id}")

        # Trimite date simulate la diverse intervale
        for _ in range(5):  # Trimite 5 mesaje pentru fiecare cerere
            temperatura = round(random.uniform(20.0, 30.0), 2)
            timestamp = datetime.now().isoformat()
            response = {
                "id_senzor": sensor_id,
                "temperatura": temperatura,
                "timp": timestamp
            }
            await websocket.send(json.dumps(response))
            await asyncio.sleep(random.uniform(0.5, 2.0))  # Așteaptă între 0.5 și 2 secunde

async def main():
    async with websockets.serve(gate_handler, "localhost", 8765):
        print("Gate process running on ws://localhost:8765")
        await asyncio.Future()  # Rulează serverul pe termen nelimitat

if __name__ == "__main__":
    asyncio.run(main())