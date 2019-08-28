import argparse
import aiohttp
from demo import create_app, async_create_app, load_config, set_config


def main():
    parser = argparse.ArgumentParser(description="Demo aiohttp project")
    parser.add_argument('--host', help='host', default='127.0.0.1')
    parser.add_argument('--port', help='port', default=5000)
    parser.add_argument('--reload', action="store_true", help="autoreload")
    parser.add_argument('--config', type=argparse.FileType('r'), help="conf file")

    args = parser.parse_args()

    app = async_create_app(load_config(args.config))

    if args.reload:
        print("Start with code reloader")
        import aioreloader
        aioreloader.start()

    aiohttp.web.run_app(app, host=args.host, port=args.port)


if __name__ == '__main__':
    main()
else:
    app = create_app(load_config())
