import React, { useState } from "react";
import axios from "axios";
import { FaCloudUploadAlt } from "react-icons/fa";

const UploadForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [aadhaarData, setAadhaarData] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setMessage("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/upload",
        formData
      );
      setAadhaarData(response.data.data);
      setMessage("Upload successful!");
    } catch (error) {
      setMessage("Upload failed. Please try again.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      {/* ✅ Upload Card */}
      <div className="bg-white shadow-lg rounded-lg p-8 w-full max-w-md text-center">
        <h2 className="text-2xl font-bold text-gray-800">
          Upload Aadhaar Image
        </h2>

        {/* ✅ File Upload Box */}
        <label
          htmlFor="fileInput"
          className="cursor-pointer mt-4 flex flex-col items-center border-2 border-dashed border-gray-300 p-6 rounded-lg hover:bg-gray-50 transition"
        >
          <FaCloudUploadAlt className="text-5xl text-blue-500" />
          <p className="text-gray-600 mt-2">Click to upload</p>
        </label>
        <input
          type="file"
          id="fileInput"
          className="hidden"
          onChange={handleFileChange}
        />

        {/* ✅ Upload Button */}
        <button
          onClick={handleUpload}
          className="mt-4 w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
        >
          Upload
        </button>

        {/* ✅ Message Display */}
        {message && <p className="mt-3 text-gray-700">{message}</p>}
      </div>

      {/* ✅ Show Extracted Aadhaar Data */}
      {aadhaarData && (
        <div className="bg-white shadow-lg rounded-lg p-6 mt-6 w-full max-w-md">
          <h3 className="text-xl font-semibold text-gray-800">
            Extracted Aadhaar Details:
          </h3>
          <p className="text-gray-700">
            <strong>Name:</strong> {aadhaarData.name}
          </p>
          <p className="text-gray-700">
            <strong>Aadhaar Number:</strong> {aadhaarData.aadhaar_number}
          </p>
          <p className="text-gray-700">
            <strong>Date of Birth:</strong> {aadhaarData.dob}
          </p>
          <p className="text-gray-700">
            <strong>Address:</strong> {aadhaarData.address}
          </p>
        </div>
      )}
    </div>
  );
};

export default UploadForm;
