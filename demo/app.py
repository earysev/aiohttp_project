from aiohttp import web
import jinja2
import aiohttp_jinja2
from . import routes


async def async_create_app(config):

    return create_app(config)


def create_app(config):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('demo', 'templates'))
    routes.setup_routes(app)
    return app


