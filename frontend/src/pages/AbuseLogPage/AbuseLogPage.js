import React from "react";
import { useEffect, useState } from "react";

import axios from "axios";
import useAuth from "../../hooks/useAuth";

const AbuseLogPage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  const [user, token] = useAuth();
  const [abuselog, setAbuseLogs] = useState([]);

  useEffect(() => {
    const fetchAbuselog = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/abuselogs/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setAbuseLogs(response.data);
      } catch (error) {
        console.log(error.message);
      }
    };
    fetchAbuselog();
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

export default AbuseLogPage;
