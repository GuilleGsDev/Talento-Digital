var nombre = prompt("Ingrese su nombre:");
var carrera = prompt("Ingrese su carrera:");

document.getElementById("nombre").innerHTML = nombre;
document.getElementById("carrera").innerHTML = carrera;

var htmlNota1 = prompt("Ingrese nota 1 [HTML]:");
var htmlNota2 = prompt("Ingrese nota 2 [HTML]:");
var htmlNota3 = prompt("Ingrese nota 3 [HTML]:");

document.getElementById("html-n1").innerHTML = htmlNota1;
document.getElementById("html-n2").innerHTML = htmlNota2;
document.getElementById("html-n3").innerHTML = htmlNota3;

var htmlPromedio = (parseFloat(htmlNota1) + parseFloat(htmlNota2) + parseFloat(htmlNota3)) / 3;

document.getElementById("html-promedio").innerHTML = htmlPromedio.toFixed(2);

var cssNota1 = prompt("Ingrese nota 1 [CSS]:");
var cssNota2 = prompt("Ingrese nota 2 [CSS]:");
var cssNota3 = prompt("Ingrese nota 3 [CSS]:");

document.getElementById("css-n1").innerHTML = cssNota1;
document.getElementById("css-n2").innerHTML = cssNota2;
document.getElementById("css-n3").innerHTML = cssNota3;

var cssPromedio = (parseFloat(cssNota1) + parseFloat(cssNota2) + parseFloat(cssNota3)) / 3;
document.getElementById("css-promedio").innerHTML = cssPromedio.toFixed(2);

var jsNota1 = prompt("Ingrese nota 1 [JavaScript]:");
var jsNota2 = prompt("Ingrese nota 2 [JavaScript]:");
var jsNota3 = prompt("Ingrese nota 3 [JavaScript]:");

document.getElementById("js-n1").innerHTML = jsNota1;
document.getElementById("js-n2").innerHTML = jsNota2;
document.getElementById("js-n3").innerHTML = jsNota3;

var jsPromedio = (parseFloat(jsNota1) + parseFloat(jsNota2) + parseFloat(jsNota3)) / 3;
document.getElementById("js-promedio").innerHTML = jsPromedio.toFixed(2);