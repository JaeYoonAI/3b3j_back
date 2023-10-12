window.onload = ()=>{
    console.log("created")
}

async function handleSignin(){
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    console.log(username, password)

    const response = await fetch('http://127.0.0.1:8000/users/signup/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "username":username,
            "password":password
        })
    })
    console.log(response)
}

async function handleLogin(){
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    console.log(username, password)

    const response = await fetch('http://127.0.0.1:8000/api/token/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "username":username,
            "password":password
        })
    })
    const response_json = await response.json()

    console.log(response_json)

    setItem("access", response_json.access);
    setItem("refresh", response_json.refresh);
}

