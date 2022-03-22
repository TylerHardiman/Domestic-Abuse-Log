// General Imports
import { Routes, Route, Outlet } from "react-router-dom";
import { Component } from "react";
import "./App.css";

// Pages Imports
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";
import HomePage from "./pages/HomePage/HomePage";
import CommentBox from "./components/CommentForum/CommentBox";

function App() {

 
  return (
    <>
      <Routes>
        {/* Routes that needs a navbar will need to go as children of this Route component */}
        <Route path="/" element={<LayoutsWithNavbar />}>
          <Route path="/" element={<div>Domestic Abuse Tracker</div>} />
          <Route path="/resources" element={<Resources Component={Resources}/>} />
          <Route path="/commentbox" element={<CommentBox component={CommentBox}/>} />
        </Route>

        {/* Routes without a navbar you can add them here as normal routes */}
        <Route
          path="/loginpage"
          element={<LoginPage component={LoginPage} />}
        />
        <Route
          path="/registerpage"
          element={<RegisterPage component={RegisterPage} />}
        />
      </Routes>
    </>
  );

  function LayoutsWithNavbar() {
    return (
      <>
        {/* Your navbar component */}
        <Navbar />
  
        {/* This Outlet is the place in which react-router will render your components that you need with the navbar */}
        <Outlet /> 
        
        {/* You can add a footer to get fancy in here :) */}
      </>
    );
  }
  


  
  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <LoginPage />
              <RegisterPage />
              <HomePage />

            </PrivateRoute>
          }
        />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/homepage" element={<HomePage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
