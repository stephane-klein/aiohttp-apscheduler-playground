"""
Demonstrates how to use the Tornado compatible scheduler to schedule a job that executes on 3
second intervals.
"""

from datetime import datetime
import os

import aiohttp
from aiohttp import web
from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    import asyncio
except ImportError:
    import trollius as asyncio


def tick():
    print('Tick! The time is: %s' % datetime.now())

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])

    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    loop = asyncio.get_event_loop()
    runner = aiohttp.web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = aiohttp.web.TCPSite(runner)
    loop.run_until_complete(site.start())

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
