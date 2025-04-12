from flask import Flask
from flask_cors import CORS
# from app.routes.forecasting import forecast_bp
# from app.routes.region_map import region_map_bp
import logging

def create_app():
    app = Flask(__name__)

    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,  # Or INFO in production
        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    app.logger.setLevel(logging.DEBUG)

    CORS(app, origins=["http://localhost:3000"])

    # Register Blueprints
    # app.register_blueprint(forecast_bp)
    # app.register_blueprint(region_map_bp)

    # You can add more config, extensions, or error handlers here later
    return app