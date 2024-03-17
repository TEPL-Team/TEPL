import React from "react";
import "./Home.css";
import Navbar from './Navbar';

function Home() {
    return (
        <div>
            <section id="home" className="home-section">
                <div className="container">
                    <h1 className="main-title">Welcome to the TEPL site!</h1>
                    <h2 className="subtitle">Where pro meets grammar...</h2>
                    <img
                        src="../teplthumbnail.png"
                        id="teplthumbnail"
                        className="tepl-thumbnail"
                    />
                    <p className="main-info">
                        TEPL is a small interpreted language that is designed to be
                        easy to learn and use.
                    </p>
                    <p className="main-info">
                        Stay tuned for updates on functions, loops, and more coming
                        by early 2025!
                    </p>
                    <p className="main-info">&copy; 2024 TEPL</p>
                </div>
            </section>
        </div>
    );
}

export default Home;
