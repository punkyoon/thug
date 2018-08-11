import json
import asyncio
import websockets

import conf
from thug import Thug


async def reborn_thug():
    thug = Thug(conf.TOKEN, conf.TRIG)
    ws = await websockets.connect(thug.endpoint)

    while True:
        msg = await ws.recv()
        json_msg = json.loads(msg)

        if json_msg['type'] == 'message':
            try:
                thug.catch_message(
                    json_msg['channel'],
                    json_msg['user'],
                    json_msg['text']
                )
            except:
                print('error')


if __name__ == '__main__':
    print('hello')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.get_event_loop().run_until_complete(reborn_thug())
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print('goodbye')
