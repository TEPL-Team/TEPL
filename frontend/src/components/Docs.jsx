import React from "react";
import "./Docs.css";

const codesnip = `OUTPUT "Enter a number: " AWAIT
INPUT EXPECTING NUM 
SET num TO INPUT
IF num % 2 == 0? THEN 
    OUTPUT num+" is an even number!" 
ELSE THEN
    OUTPUT num+" is an odd number!" 
END IF`;

function Docs() {
    return (
        <section class="docs-section">
            <div class="container">
                <h1 class="main-title">TEPL Documentation</h1>

                <div class="warning">
                    <p>
                        ⚠️ This interpreter is currently in development, so it
                        might have breaking changes with each update.
                    </p>
                </div>

                <div class="feedback">
                    <p>
                        💬 Got some questions or feedback? Just open an issue                <a href="https://github.com/TENTHER101/TEPL/discussions/categories/q-a">here</a>                    and we'll be glad to respond!
                    </p>
                </div>

                <pre class="code-sample">
                    <code>{codesnip}</code>
                </pre>

                <p class="main-info">
                    TEPL is a scripting programming language in development that
                    strives to make coding simple, easy, and fun to learn. It
                    comes with many features, including:
                </p>

                <div class="toc">
                    <h2 class="toc-title">Table of Contents</h2>
                    <ul class="toc-list">
                        <li>
                            <a href="#intro">Introduction</a>
                        </li>
                        <li>
                            <a href="#install">Installation</a>
                        </li>
                        <li>
                            <a href="#files-and-the-code-panel">
                                Files and the Code Panel
                            </a>
                        </li>
                        <li>
                            <a href="#output">OUTPUT</a>
                        </li>
                    </ul>
                </div>
                <div id="intro" class="section-content">
                    <h3>Introduction</h3>
                    <p>
                        Welcome fellow programmers or soon-to-be programmers!
                        This guide aims to thoroughly explain how TEPL works.
                        TEPL is a basic programming language with many features
                        designed to teach the basic concepts of programming. It
                        is especially useful for beginners and teachers looking
                        to introduce programming in a clear and simple manner.
                    </p>
                </div>

                <div id="install" class="section-content">
                    <h3>Installation</h3>
                    <p>
                        If you wish to view the source code and edit it,
                        download the <code>lexer.py</code>,
                        <code>parser.py</code>, <code>interpreter.py</code>, and
                        <code>main.py</code> files. You can also download the
                        executable file
                        <a href="https://tepl.vercel.app/download.html">here</a>
                        .
                    </p>
                    <pre>pip install -r requirements.txt</pre>
                    <p>
                        To start the program, run the <code>main.py</code> file.
                    </p>
                </div>

                <div class="faq-section">
                    <h2>FAQ</h2>
                    <h3>When will TEPL be ready to use?</h3>
                    <p>
                        We aim to have TEPL ready by the end of 2024 or possibly
                        sooner. Currently, we are building the base syntax and
                        will move on to more advanced functionalities and
                        important features. Libraries and frameworks will also
                        be added in the future.
                    </p>

                    <h3>Why use TEPL?</h3>
                    <p>
                        TEPL is designed for beginners and focuses on backend
                        development. Although it currently lacks frontend
                        features, we plan to introduce VEPL (Visually
                        Educational Programming Language) for frontend
                        development. TEPL uses simple and English-like grammar,
                        making it easy for beginners to learn.
                    </p>
                    <pre>FUNCTION add a b MEANS RETURN a+b END</pre>
                    <p>
                        (Disclaimer: the syntax shown above is subject to
                        change, but the idea of functions will be introduced
                        later on.)
                    </p>

                    <h3>License</h3>
                    <p>
                        TEPL is licensed under the Apache License for enhanced
                        security. We hope that this software will inspire other
                        projects and contribute to the improvement of software
                        quality.
                    </p>

                    <h3>Credits</h3>
                    <p>
                        Credits to everyone who contributed! We have received
                        help from various resources and even AI. The inspiration
                        for TEPL comes from the needs in our society, and we
                        credit everyone for their support.
                    </p>
                </div>
            </div>
        </section>
    );
}

export default Docs;
