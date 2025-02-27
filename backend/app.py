from flask import Flask
from flask_cors import CORS
from backend.config import Config
from backend.extensions import db, migrate
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config["UPLOAD_FOLDER"] = "backend/photos"

# ✅ Enable CORS for frontend at http://localhost:3000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# ✅ Initialize database & migration
db.init_app(app)
migrate.init_app(app, db)

# ✅ Ensure Upload Folder Exists
if not os.path.exists("backend/photos"):
    os.makedirs("backend/photos")

# ✅ Register blueprints
def register_blueprints():
    from backend.routes.upload import upload_blueprint
    app.register_blueprint(upload_blueprint, url_prefix="/api")

register_blueprints()

# ✅ Run Flask on 127.0.0.1:5000
if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database tables checked/created successfully.")
        except Exception as e:
            print(f"❌ Database initialization error: {e}")

    app.run(debug=True, host="127.0.0.1", port=5000)
