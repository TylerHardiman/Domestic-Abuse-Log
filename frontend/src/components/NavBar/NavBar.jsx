import React from "react";
import { useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import "./NavBar.css";

const Navbar = () => {
  const { logoutUser, user } = useContext(AuthContext);
  const navigate = useNavigate();
  return (
    <div className="navBar">
      <ul>
      <li className='mr-auto mb-2 mb-lg-0'>
          <Link to="/" style={{ textDecoration: "none", color: "white" }}>
            <b>Domestic Abuse Tracker</b>
          </Link>
          <br>
          </br>      
          <Link to="/resourcepage" style={{ textDecoration: "none", color: "white" }}>
            <b>Resources</b>
          </Link>
          <br>
          </br>
          <Link to="/commentbox" style={{ textDecoration: "none", color: "white" }}>
            <b>Support Forum</b>
          </Link>
        </li>
        <li>
          {user ? (
            <button onClick={logoutUser}>Logout</button>
          ) : (
            <button onClick={() => navigate("/login")}>Login</button>
          )}
        </li>
      </ul>
    </div>
  );
};

export default Navbar;
