from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import budget, pac
    app.register_blueprint(budget.bp, url_prefix='/tools/budget')
    app.register_blueprint(pac.bp, url_prefix='/tools/pac')

    return app
