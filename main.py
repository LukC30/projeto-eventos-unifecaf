from flask import Flask

from api.event_route import event_api
from api.user_route import user_api

def create_app():
    """
    Função utilizada para criar a instancia do Flask
    """
    app = Flask(__name__)

    app.register_blueprint(event_api, url_prefix='/api')
    app.register_blueprint(user_api, url_prefix="/api")
    @app.route('/', methods=["GET"])

    def index():
        return "API DO SISTEMA ESTÁ FUNCIONANDO!!!!"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)