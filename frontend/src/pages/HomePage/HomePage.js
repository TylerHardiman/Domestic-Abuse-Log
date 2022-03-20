import React from "react";
import { useEffect, useState } from "react";

import axios from "axios";
import useAuth from "../../hooks/useAuth";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  const [user, token] = useAuth();
  const [survivor, setSurvivors] = useState([]);

  useEffect(() => {
    const fetchSurvivors = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/survivors/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setSurvivors(response.data);
      } catch (error) {
        console.log(error.message);
      }
    };
    fetchSurvivors();
  }, [token]);
  return (
    <div className="container">
      <h1>You are stronger then you know {user.username}!</h1>
      {survivor &&
        survivor.map((survivor) => (
          <p key={survivor.id}>
            {survivor.first_name} {survivor.last_name} {survivor.email}
          </p>
        ))}
    </div>
  );
};

export default HomePage;
