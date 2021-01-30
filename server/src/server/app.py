from flask import Flask, jsonify

import server


def main():
    create_app().run()


def create_app():
    app = Flask(__name__)

    @app.route("/version")
    def version():
        return jsonify(Version=server.__version__)

    @app.route("/classify")
    def hello_world():
        return jsonify(Survived=0)

    @app.route("/")
    def hello():
        return "Hi!"

    return app


if __name__ == "__main__":
    main()
