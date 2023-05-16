let socket = new WebSocket("ws://localhost:5000");

socket.onmessage = function (event) {
    let div = document.getElementById("msgs");
    div.innerHTML = `<p>${event.data}</p>`;
}

function enviar() {
    let msg = document.getElementById("msg");
    socket.send(msg.value);
    msg.value = "";
}