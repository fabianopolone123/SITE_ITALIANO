function speakItalian(text) {
    if (!("speechSynthesis" in window)) {
        return;
    }

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "it-IT";
    utterance.rate = 0.86;
    window.speechSynthesis.speak(utterance);
}

document.addEventListener("click", (event) => {
    const button = event.target.closest(".speak-button");
    if (!button) {
        return;
    }
    speakItalian(button.dataset.speak || "");
});
