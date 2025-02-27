from backend.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadhaar_number = db.Column(db.String(20), unique=True, nullable=False)
    photo_path = db.Column(db.String(200), nullable=False)  # ✅ Stores only Aadhaar image path
