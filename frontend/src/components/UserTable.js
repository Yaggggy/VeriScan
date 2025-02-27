import React, { useState, useEffect } from "react";
import axios from "axios";

const UserTable = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/get_users")
      .then((response) => setUsers(response.data))
      .catch((error) => console.error("Error fetching users:", error));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold text-gray-800 text-center mb-4">
          Registered Aadhaar Users
        </h2>

        <div className="overflow-x-auto">
          <table className="w-full border-collapse bg-white shadow-md rounded-lg">
            <thead>
              <tr className="bg-gray-200 text-gray-700">
                <th className="p-3 text-left">Name</th>
                <th className="p-3 text-left">Aadhaar Number</th>
                <th className="p-3 text-left">Date of Birth</th>
                <th className="p-3 text-left">Address</th>
                <th className="p-3 text-left">Photo</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr
                  key={user.id}
                  className="border-t text-gray-700 hover:bg-gray-100 transition"
                >
                  <td className="p-3">{user.name}</td>
                  <td className="p-3">{user.aadhaar_number}</td>
                  <td className="p-3">{user.dob}</td>
                  <td className="p-3">{user.address}</td>
                  <td className="p-3">
                    <img
                      src={`http://127.0.0.1:5000/${user.photo_path}`}
                      alt="User"
                      className="w-20 h-20 object-cover rounded-lg shadow-md"
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default UserTable;
