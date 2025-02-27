from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
CORS(app)

# Import and register routes
from routes.id_processing import id_blueprint
app.register_blueprint(id_blueprint, url_prefix="/api")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ✅ Now runs within the app context
    app.run(debug=True)
