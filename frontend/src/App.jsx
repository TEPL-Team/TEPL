import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Help from "./components/Help";
import Download from "./components/Download";
import Docs from "./components/Docs";
import NotFound from "./components/NotFound";
import { Analytics } from "@vercel/analytics/react";

function App() {
    return (
        <Router>
            <Analytics />
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="about" element={<About />} />
                <Route path="help" element={<Help />} />
                <Route path="download" element={<Download />} />
                <Route path="docs" element={<Docs />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </Router>
    );
}

export default App;
