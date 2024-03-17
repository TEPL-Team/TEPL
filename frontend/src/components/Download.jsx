import React from "react";
import "./Download.css";
import Popup from "reactjs-popup";

function Download() {
    return (
        <section id="download" class="download-section">
            <div class="container">
                <h1 class="main-title">Download TEPL</h1>
                <Popup
                    trigger={
                        <button className="download-link">
                            {" "}
                            Download TEPL version 0.75.0{" "}
                        </button>
                    }
                    modal
                    nested
                >
                    {(close) => (
                        <div className="container">
                            <div>
                                This Download is not yet available, come back
                                another time!
                            </div>
                            <div>
                                <button onClick={() => close()}>Close</button>
                            </div>
                        </div>
                    )}
                </Popup>
            </div>
        </section>
    );
}

var downloads = {
    v0750: document.getElementById("download-v-0750"),
};

export default Download;
