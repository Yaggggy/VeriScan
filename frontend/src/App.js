import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import UploadForm from "./components/UploadForm";
import UserTable from "./components/UserTable";

function App() {
  return (
    <Router>
      {/* ✅ Navbar */}
      <header className="bg-blue-600 text-white py-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center px-6">
          <h1 className="text-2xl font-bold">VeriScan</h1>
          <nav className="space-x-6">
            <Link to="/" className="hover:underline">
              Upload Aadhaar
            </Link>
            <Link to="/users" className="hover:underline">
              View Users
            </Link>
          </nav>
        </div>
      </header>

      {/* ✅ Page Content */}
      <main className="flex-grow container mx-auto p-6">
        <Routes>
          <Route path="/" element={<UploadForm />} />
          <Route path="/users" element={<UserTable />} />
        </Routes>
      </main>

      {/* ✅ Footer */}
      <footer className="bg-gray-900 text-white text-center py-4 mt-6">
        <p>&copy; 2025 VeriScan. All rights reserved.</p>
      </footer>
    </Router>
  );
}

export default App;
