# VeriScan - Aadhaar Verification System

## 📌 Project Overview

VeriScan is an advanced **Aadhaar verification system** that extracts and verifies Aadhaar numbers from uploaded Aadhaar card images using **OCR (Optical Character Recognition)**. The extracted Aadhaar numbers are stored securely in a database for authentication.

This project is designed to be **integrated with the Smart Queue Reduction System**, where Aadhaar-based user registration can be used for identity verification before allowing access.

## 🎯 Project Aim

- **Automate Aadhaar number extraction** from images.
- **Enhance security & efficiency** in Aadhaar-based verification.
- **Integrate with Smart Queue Reduction System** for facial recognition-based authentication.
- **Ensure high OCR accuracy** using **Tesseract & EasyOCR**.

---

## 📂 Project Structure

```
VeriScan/
│── backend/
│   ├── routes/
│   │   ├── upload.py      # Handles file upload & Aadhaar extraction
│   ├── models/
│   │   ├── user.py       # User database model
│   ├── services/
│   │   ├── ocr_extraction.py  # Extracts Aadhaar number using OCR
│   ├── extensions.py      # Database extensions
│   ├── config.py         # Configuration settings
│   ├── app.py           # Main Flask application
│   ├── database/
│   │   ├── veriscan.db   # SQLite Database
│   ├── photos/          # Stores uploaded Aadhaar images
│── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadForm.js  # React file upload component
│   │   ├── App.js         # Main React App
│   ├── public/
│   ├── package.json      # React dependencies
│── README.md             # Project documentation
```

---

## 🛠️ Technologies Used

### **Backend (Flask API)**

- **Flask** - Web framework
- **Flask-CORS** - Enables communication between backend & frontend
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Migrate** - Database migration
- **Tesseract OCR** - Text extraction from images
- **EasyOCR** - Advanced image text recognition

### **Frontend (ReactJS)**

- **React.js** - User Interface
- **Axios** - API communication
- **React Icons** - UI enhancement

### **Database**

- **SQLite** - Stores Aadhaar numbers & image paths securely

---

## 📦 Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Yaggggy/VeriScan.git
cd VeriScan
```

### **2️⃣ Setup Backend (Flask)**

```bash
cd backend
pip install -r requirements.txt  # Install dependencies
flask db upgrade  # Setup database
python -m backend.app  # Run the backend
```

### **3️⃣ Setup Frontend (React)**

```bash
cd frontend
npm install  # Install dependencies
npm start  # Run React frontend
```

---

## 🚀 How It Works

1️⃣ **User uploads an Aadhaar card image via the frontend UI.**
2️⃣ **Flask backend processes the image using OCR (Tesseract & EasyOCR).**
3️⃣ **Aadhaar number is extracted & stored in the database.**
4️⃣ **The extracted Aadhaar number is displayed on the frontend.**
5️⃣ **Integration with the Queue Reduction System allows Aadhaar-based user registration for facial recognition authentication.**

---

## ⚙️ API Endpoints

### ✅ **Upload Aadhaar Image**

**Endpoint:** `/api/upload`\
**Method:** `POST`\
**Request:**

```bash
curl -X POST -F "file=@aadhaar.jpg" http://127.0.0.1:5000/api/upload
```

**Response:**

```json
{
    "message": "Upload successful!",
    "aadhaar_number": "2331 xxxx xxxx"
}
```

---

## 🔥 Future Enhancements

- ✅ **Improve OCR accuracy** using Deep Learning.
- ✅ **Integrate Facial Recognition** for Aadhaar-based authentication.
- ✅ **Deploy to AWS** for cloud-based verification.
- ✅ **Enable multi-user support** for large-scale verification.

---

## 🤝 Contributing

Want to improve VeriScan? **Feel free to fork, submit issues, and contribute!**

```bash
git clone https://github.com/Yaggggy/VeriScan.git
```

---

##

