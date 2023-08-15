const lupa = document.querySelector("#lupa");
let lupaClicked = false;

lupa.addEventListener("click", () => {
    lupaClicked = !lupaClicked;
    lupa.style.backgroundColor = lupaClicked ? "rgba(255, 0, 0, 0.2)" : "";

    if (lupaClicked) {
        document.addEventListener("mousemove", onMouseMove);
        document.addEventListener("mouseout", onMouseOut);
    } else {
        document.removeEventListener("mousemove", onMouseMove);
        document.removeEventListener("mouseout", onMouseOut);
        resetFontSize();
    }
});

function onMouseMove(e) {
    const x = e.clientX;
    const y = e.clientY;
    const elements = document.elementsFromPoint(x, y);

    for (const element of elements) {
        if (isTextElement(element) || isButtonElement(element)) {
            element.style.fontSize = "150%";
        }
    }
}

function onMouseOut(e) {
    const relatedTarget = e.relatedTarget;

    if (!relatedTarget || (!isTextElement(relatedTarget) && !isButtonElement(relatedTarget))) {
        resetFontSize();
    }
}

function isTextElement(element) {
    return ["P", "H1", "H2", "H3", "H4", "H5", "H6", "SPAN", "DIV" , "a"].includes(element.tagName);
}

function isButtonElement(element) {
    return element.tagName === "I" || element.tagName === "INPUT" && element.type === "submit";
}

function resetFontSize() {
    const textElements = document.querySelectorAll("p, h1, h2, h3, h4, h5, h6, span, div, i, input[type='submit'], a");

    for (const element of textElements) {
        element.style.fontSize = "100%";
    }
}
