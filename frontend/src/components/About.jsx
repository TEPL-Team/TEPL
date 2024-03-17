import React from "react";
import "./About.css";

const sn = '${num}';

const codesnip = `FUNCTION add a b MEANS 
    RETURN a+b 
END add 

REPEAT 5 TIMES AS i 
    OUTPUT i 
END REPEAT 

SET i TO 0 
WHILE 5 > i REPEAT 
    OUTPUT i
    SET i TO i + 1 
END REPEAT 

OUTPUT "Enter a number: " AWAIT
INPUT EXPECTING NUM 
SET num TO INPUT 

IF num > 10? THEN
    OUTPUT "Num is greater than ten!" 
ELSEIF num > 50? THEN
    OUTPUT "Num is greater than 50!" ELSE? THEN OUTPUT $"Num is ${sn}" 
END IF`;

function About() {
    return (
        <section id="about" class="about-section">
            <div class="container">
                <h1 class="main-title">About TEPL</h1>
                <h2 class="subtitle">
                    Textual Educational Programming Language
                </h2>
                <p class="main-info">
                    TEPL is a language designed for educational purposes,
                    focusing on simplicity and ease of learning.
                </p>
                <p class="main-info">
                    It aims to help beginners understand programming concepts in
                    a clear and concise manner.
                </p>
                <img
                    src="../teplthumbnail.png"
                    id="teplthumbnail"
                    class="tepl-thumbnail"
                />
                <h2 class="subtitle">The Future of TEPL</h2>
                <p class="main-info">
                    We plan to finish the basics of TEPL by early 2025,
                    including functions, for loops, while loops, and
                    if-elseif-else statements.
                </p>
                <h3 class="subtitle">Grammar Examples (Future Additions)</h3>
                <pre class="code-sample">
                    <code>{codesnip}</code>
                </pre>
                <h2 class="subtitle">Contact Us</h2>
                <p class="main-info">
                    Have questions or feedback? Feel free to reach out to us at                  <a href="mailto:valuex.programmer.ces@gmail.com">
                         valuex.programmer.ces@gmail.com
                    </a>
                </p>
            </div>
        </section>
    );
}

export default About;
