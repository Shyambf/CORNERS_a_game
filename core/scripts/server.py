import websockets
from websockets.sync.client import connect as con
import asyncio
import pygame
from core.scripts.config import PORT, IPADDRESS
import numpy as np
import time

EVENTTYPE = pygame.event.custom_type()

# handler processes the message and sends "Success" back to the client
async def handler(websocket, path):
    async for message in websocket:
        processMsg(message, websocket)

def processMsg(message, websocket):
    print(f"[Received]: {message}")
    with open('core/src/temp.txt', 'w+') as file:
        file.write(message)
    pygame.fastevent.post(pygame.event.Event(EVENTTYPE, message=(message, websocket)))


def client(maps):
    with con(f'ws://{IPADDRESS}:{PORT}/') as websocket:
        print('Подключенно к серверу')
        websocket.send(''.join(map(str, list(np.array(maps).flatten()))))
        response = websocket.recv()
        print(response)
        pygame.fastevent.post(pygame.event.Event(EVENTTYPE, message=(list(np.array([int(response[i]) for i in range(64)]).reshape((8, 8))))))

async def send_map(maps, web):
    await web.send(''.join(map(str, list(np.array(maps).flatten()))))

async def main(future):
    async with websockets.serve(handler, IPADDRESS, PORT):
        print('server start')
        await future  # run forever

if __name__ == "__main__":
    asyncio.run(main())