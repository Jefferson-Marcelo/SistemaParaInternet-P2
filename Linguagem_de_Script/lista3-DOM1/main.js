//Primeira Questão
let temperatura = "";
function result(){    
    temperatura = document.getElementById("temperatura").value
    let tempEmFeirenheit = celsiusFerenheit(temperatura)
    let tempEmKelvin = celsiusKelvin(temperatura)
    document.getElementById("Farenheit").innerHTML = tempEmFeirenheit
    document.getElementById("Kelvin").innerHTML = tempEmKelvin
}

function celsiusFerenheit(num){
    let ferenheit = (num*1.8)+32
    return `A temperatura em Ferenheit é de ${ferenheit}`
}

function celsiusKelvin(num){
    let kelvin = ((num-32)/1.8)+273.15
    return `A temperatura em Kelvin é de ${kelvin}`
}

//Segunda questão

function letraA(){
    let windowWidth = window.innerWidth;
    document.getElementById("alternativaA").value = windowWidth
}

function letraB(){
    let windowHeight = window.innerHeight;
    document.getElementById("alternativaB").value = windowHeight
}

function letraC(){
    let larg = document.getElementById("largura").value
    let alt = document.querySelector("#altura").value
    window.resizeTo(larg,alt)
    window.focus()
    console.log(larg)
    console.log(alt)
}

function letraD(){
    window.close()
}

function fundoAmarelo(){
    let nome = document.getElementById("trabalharTexto")    
    let separador = nome.innerHTML.split(' ')          
    let filtro = palavra => {
        if(palavra.length>8){
            return `<span class="destaque">${palavra}</span>`
        }else{
            return palavra
        }
    }
    let result = separador.map(filtro).join(' ')                 
    nome.innerHTML = result
    return nome          
}

