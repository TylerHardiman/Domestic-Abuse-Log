import React from "react";
import { useEffect, useState } from "react";

import axios from "axios";
import useAuth from "../../hooks/useAuth";

const UserPage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  const [user, token] = useAuth();
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/UserPage/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setUsers(response.data);
      } catch (error) {
        console.log(error.message);
      }
    };
    fetchUsers();
  }, [token]);
  return (
    <div className="container">
      <h1>You are stronger then you know {user.username}!</h1>
      {user &&
        user.map((user) => (
          <p key={user.id}>
            {user.first_name} {user.last_name} {user.email}
          </p>
        ))}
    </div>
  );
};

export default UserPage;
