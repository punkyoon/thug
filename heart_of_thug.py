import json
import asyncio
import websockets

from conf import *
from thug import Thug


async def reborn_thug():
    ws = await websockets.connect(sock_endpoint)
    thug = Thug(conf.TOKEN, conf.TRIG)

    while True:
        msg = await ws.recv()
        json_msg = json.loads(msg)

        if json_msg['type'] == 'message':
            try:
                thug.catch_message(
                    json_msg['channel'],
                    json_msg['text'],
                    json_msg['user']
                )
             except:
                print('error')


if __name__ == '__main__':
    slack = Slacker(TOKEN)
    resposne = slack.rtm.start()
    endpoint = response.body['url']

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(reborn_thug())
    asyncio.get_event_loop().run_forever()
