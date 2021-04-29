function myFunction(){
const Http = new XMLHttpRequest();
const url='http://127.0.0.1:5000/pattern';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
}