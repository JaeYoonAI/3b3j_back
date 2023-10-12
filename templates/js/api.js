window.onload = ()=>{
    console.log("loaded")
}

async function handleSignin(){
    const email = document.getElementById("email").value
    const nickname = document.getElementById("nickname").value
    const password = document.getElementById("password").value
    console.log(email, nickname, password)

    const response = await fetch("http://127.0.0.1:8000/users/signup_api/", {
        headers:{
            "content-type": "application/json",
        },
        method: 'POST',
        body: JSON.stringify({
            "email":"email",
            "nickname":"nickname",
            "password":"password"
        })
    })

    console.log(response)
}