import asyncio
import websockets
import json
import random

async def send_requests():
    uri = "ws://localhost:8765"
    sensor_ids = [121, 141, 111]

    async with websockets.connect(uri) as websocket:
        for _ in range(3):  # Trimite câte o cerere pentru fiecare senzor
            sensor_id = random.choice(sensor_ids)
            request = {"id_senzor": sensor_id}
            print(f"Sending request for sensor ID: {sensor_id}")
            await websocket.send(json.dumps(request))

            # Așteaptă răspunsurile gateway-ului
            for _ in range(5):  # Așteaptă 5 răspunsuri per cerere
                response = await websocket.recv()
                print(f"Received: {response}")
            await asyncio.sleep(random.uniform(1, 3))  # Așteaptă între cereri

if __name__ == "__main__":
    asyncio.run(send_requests())