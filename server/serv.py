import asyncio
from aiohttp import web
import paho.mqtt.client as mqtt
import json
import websockets

IP = "winnieliu.ddns.net"

FILE_PATH = './public'
MAIN_INDEX = '/index.html'

PORT = 11230 #web port

async def HomePage(request):
    return web.FileResponse(FILE_PATH + '/index.html')
#return web.Response(text="ok",content_type='text/html')


async def ChangeDirection(request):
    direction = request.rel_url.query['dir']
    print(direction)
    return web.Response(text="ok",content_type='text/html')

async def init(loop):
    app = web.Application()
    app.router.add_static('/public','./public')
    
    #receiving request
    app.router.add_get('/',HomePage)
    app.router.add_get('/change_dir',ChangeDirection)
    srv = await loop.create_server(app._make_handler(),host='0.0.0.0', port=PORT)
    print("server created")
    return srv

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(init(loop))

        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
