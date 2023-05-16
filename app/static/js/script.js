let socket = io.connect("http://localhost:5000/chat")
socket.on("connect", function () {
    socket.emit("entrada");
});

socket.on("status", function(dados) {
    let div = document.getElementById("msgs");
    div.innerHTML += `<p>${dados['msg']}</p>`;
});

socket.on("msg", function(dados) {
    let div = document.getElementById("msgs");
    div.innerHTML += `<p>${dados['msg']}</p>`;
});

function enviar() {
    let msg = document.getElementById("msg");
    socket.emit("msg", {"msg": msg.value});
    msg.value = "";
}

function desconectar(url) {
    socket.emit("saida", {}, function () {
        socket.disconnect();
        window.location.href = url;
    })
}