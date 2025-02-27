from flask import Flask
from flask_cors import CORS
from backend.config import Config  # ✅ Corrected Import
from backend.extensions import db, migrate

app = Flask(__name__)
app.config.from_object(Config)  # ✅ Uses Config class directly
app.config["UPLOAD_FOLDER"] = "backend/photos"

# ✅ Enable CORS once (only for /api routes)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# ✅ Initialize database & migration
db.init_app(app)
migrate.init_app(app, db)

# ✅ Lazy import blueprints AFTER initializing Flask
def register_blueprints():
    from backend.routes.id_processing import id_blueprint
    from backend.routes.upload import upload_blueprint
    from backend.routes.user import user_blueprint

    app.register_blueprint(id_blueprint, url_prefix="/api")
    app.register_blueprint(upload_blueprint, url_prefix="/api")
    app.register_blueprint(user_blueprint, url_prefix="/api")

register_blueprints()

# ✅ Run the application safely
if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()  # ✅ Ensures database is created
            print("✅ Database tables checked/created successfully.")
        except Exception as e:
            print(f"❌ Database initialization error: {e}")
    
    # ✅ Run Flask on 127.0.0.1:5000
    app.run(debug=True, host="127.0.0.1", port=5000)
