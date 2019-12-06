from aiohttp import web
from .views import frontend


def setup_routes(app: web.Application):
    app.router.add_route('GET', '/aiohttp/', frontend.index)
