import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="topnav">
      <div className="container">
        <Link to="/">Home</Link>
        <Link to="/help">Help</Link>
        <Link to="/about">About</Link>
        <Link to="/download">Download</Link>
      </div>
    </nav>
  );
}

export default Navbar;
