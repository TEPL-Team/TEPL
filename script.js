import { Analytics } from "@vercel/analytics/react";
//importing vercel analystics ^

var downloads = {
    v0750: document.getElementById("download-v-0750"),
};

downloads.v0750.addEventListener("click", function () {
    alert("This Download is not yet available, come back another time!");
});
