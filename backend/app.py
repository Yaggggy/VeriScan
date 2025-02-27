from flask import Flask
from flask_cors import CORS
from backend import config
from backend.extensions import db, migrate  # ✅ Import from extensions.py

app = Flask(__name__)
app.config.from_object(config.Config)

db.init_app(app)
migrate.init_app(app, db)
CORS(app)

# ✅ Lazy import blueprints AFTER Flask is initialized
def register_blueprints():
    from backend.routes.id_processing import id_blueprint
    from backend.routes.upload import upload_blueprint
    from backend.routes.user import user_blueprint  # ✅ Correct import

    app.register_blueprint(id_blueprint, url_prefix="/api")
    app.register_blueprint(upload_blueprint, url_prefix="/api")
    app.register_blueprint(user_blueprint, url_prefix="/api")

register_blueprints()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
