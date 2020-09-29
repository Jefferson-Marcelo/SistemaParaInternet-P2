/*1. Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. Após isso, defina um caractere (vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere. */

let word = 'Eu sou um cara legal'

const fatiador = palavra => palavra.split('')
const vogal = nome =>{    
    if ((nome == 'a') || (nome == 'e') || (nome == 'i') || (nome == 'o') || (nome == 'u') || (nome == 'A') || (nome == 'E') || (nome == 'I') || (nome == 'O') || (nome == 'U'))
        return true;
    else
        return false;
}
const tamanho = conta => conta.length
let sentenca = fatiador(word)
let filtrando = sentenca.filter(vogal)
let substituicao = word.replace(/['aeiouAEIOU']/g, '$')

console.log(`A frase tem: ${tamanho(filtrando)} vogais`)
console.log(substituicao)


