window.onload = ()=>{
    console.log("loaded")
}

async function handleSignin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    console.log(email, password)

    const response = await fetch("http://127.0.0.1:8000/users/api/token/", {
        headers:{
            "content-type": "application/json",
        },
        method: 'POST',
        body: JSON.stringify({
            "email":"email",
            "password":"password"
        })
    })

    console.log(response)
}