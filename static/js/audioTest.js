function hasGetUserMedia() {
    return !!(navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia ||
        navigator.msGetUserMedia);
}

if (hasGetUserMedia()) {

} else {
    alert("Audio is not supported.")
}


