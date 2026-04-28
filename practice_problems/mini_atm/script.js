function updateOutput(msg) {
    document.getElementById("output").innerText = msg;
}

function checkBalance(){
    fetch("http://127.0.0.1:5000/balance", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
    .then(data => updateOutput(data.message));
}

function createAccount(){
    fetch("http://127.0.0.1:5000/create",{
        method:"POST",
        headers: {"Content-Type": "application/json"},
    })
    .then(res=>res.json())
    .then(data => updateOutput(data.message));
}

function deposit(){
     fetch("http://127.0.0.1:5000/deposit",{
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body:JSON.stringify({amount:parseFloat(document.getElementById("amount").value)})
    })
    .then(res => res.json())
    .then(data => updateOutput(data.message));
}

function withdraw(){
    fetch("http://127.0.0.1:5000/withdraw",{
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body:JSON.stringify({amount:parseFloat(document.getElementById("amount").value)})
    })
    .then(res => res.json())
    .then(data => updateOutput(data.message));
}