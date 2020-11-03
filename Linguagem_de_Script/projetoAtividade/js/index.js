console.log('a) Capture e exiba os textos de 4 elementos de interface projetada')
let primeiroH1 = document.querySelector("h1").innerText
console.log(primeiroH1)
let primeiroP = document.querySelector("p").innerHTML
console.log(primeiroP)
let primeiroH3 = document.querySelector("h3").innerHTML
console.log(primeiroH3)
let primeiroSpan = document.querySelector("span").innerHTML
console.log(primeiroSpan)

console.log('b) Capture pelo id e exiba 2 elementos de interface projetada')
let colaboradores = document.getElementById("colab").textContent
console.log(colaboradores)
let contato = document.getElementById("city").textContent
console.log(`${contato}    ...Apareceu vazio porque é campo input`)

console.log('c) Capture pelo estilo (class) e exiba 2 elementos de interface projetada')

let colab1 = document.querySelector(".colaboradorUm").innerHTML
console.log(colab1)
let colab2 = document.querySelector(".colaboradorDois").innerHTML
console.log(colab2)

console.log('Capture exiba o texto de um elemento pela combinação tag e id (ou classe)')
let cadastro = document.querySelector("h1#cadastro").innerHTML
console.log(cadastro)
let colab3 = document.querySelector("p.colaboradorTres").innerHTML
console.log(colab3)

console.log('Modifique os textos de 2 elementos (Uma das modificações é adicionar Aula JS no title)')

function modificar1(){
    let titulo = document.querySelector("title")    
    let substituir = 'Aula JS'
    titulo.innerText = substituir    
}

function modificar2(){
    let paragrafo = document.querySelector("p")    
    let substituir = 'Fim da atividade. Obrigado professora, tem sido divertido aprender DOM'
    paragrafo.innerText = substituir    
}
