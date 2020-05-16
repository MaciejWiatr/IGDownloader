import isURL from "validator/lib/isURL";

const loadingWrapper = document.querySelector(".loading__wrapper");
const downloadForm = document.querySelector(".download__form");

const downloadFromPath = (path) => {
    const link = document.createElement("a");
    link.href = path;
    link.target = "_blank";
    link.setAttribute("download", "");
    console.log(link);
    link.click();
    loadingWrapper.style.animationName = "fade-out";
};

const fetchImg = async (url) => {
    try {
        loadingWrapper.style.animationName = "fade-in";
        const resp = await fetch(`/download/?url=${url}`);
        const data = await resp.json();
        if (data.status === 200) {
            downloadFromPath(data.path);
        } else {
            loadingWrapper.style.animationName = "fade-out";
        }
    } catch (e) {
        loadingWrapper.style.animationName = "fade-out";
        console.log("Error: ", e)
    }


};

downloadForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const elements = e.target.elements;
    const url = elements.downloadURL.value;
    if (isURL(url)) {
        fetchImg(url);
    }
});
