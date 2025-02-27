from backend.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    aadhaar_number = db.Column(db.String(12), unique=True, nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)
    photo_path = db.Column(db.String(255), nullable=False)

    def __init__(self, name, aadhaar_number, dob, address, photo_path):
        self.name = name
        self.aadhaar_number = aadhaar_number
        self.dob = dob
        self.address = address
        self.photo_path = photo_path
