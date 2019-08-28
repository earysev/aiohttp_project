from aiohttp import web
import jinja2
import aiohttp_jinja2
from . import routes


async def create_app(config: dict = None):
    app = web.Application()
    if config is None:
        pass
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('demo', 'templates'))
    routes.setup_routes(app)
    return app
