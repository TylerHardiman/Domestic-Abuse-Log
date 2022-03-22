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
      {abuselog &&
        abuselog.map((abuselog) => (
          <p key={abuselog.id}>
            {abuselog.log} {abuselog.post} {abuselog.name} {abuselog.log}
            {abuselog.email} {abuselog.body} {abuselog.created_on} {abuselog.active}
            
          </p>
        ))}
    </div>
  );
};

export default AbuseLogPage;
