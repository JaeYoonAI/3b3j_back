window.onload = ()=>{
    console.log("loaded")
}

fetch("http://127.0.0.1:8000/contents/movie/")
  .then((response) => response.json())
  .then((data) => console.log(data));

fetch("http://127.0.0.1:8000/contents/music/")
  .then((response) => response.json())
  .then((data) => console.log(data));  

fetch("http://127.0.0.1:8000/contents/game/")
  .then((response) => response.json())
  .then((data) => console.log(data)); 