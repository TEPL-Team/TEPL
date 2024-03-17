import React from "react";
import "./Help.css";

function Help() {
    return (
        <section class="help-section">
            <div class="container">
                <h1 class="main-title">Help Page</h1>
                <div class="toc">
                    <h2 class="centeredtext">Table of contents:</h2>
                    <ul class="toc-list">
                        <li class="toc-item">
                            <a href="/docs" class="toc-link">
                                Documentation
                            </a>
                        </li>
                        <li class="toc-item">
                            <a
                                href="https://github.com/TENTHER101/TEPL/discussions"
                                class="toc-link"
                            >
                                Community
                            </a>
                        </li>
                        <li class="toc-item">
                            <a href="#Tutorials" class="toc-link">
                                Tutorials
                            </a>
                        </li>
                        <li class="toc-item">
                            <a href="#FAQ" class="toc-link">
                                FAQ
                            </a>
                        </li>
                        <li class="toc-item">
                            <a href="about.html#Contact-Us" class="toc-link">
                                Contact Us
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
    );
}

export default Help;
