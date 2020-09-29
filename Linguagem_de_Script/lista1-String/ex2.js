/*2. Implemente um programa que preencha uma lista de string com os modelos de cinco carros (exemplos de modelos: Fusca, HB20, Civic, etc.). Em seguida, preencha um vetor com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre: 

(a) O modelo de carro mais econômico; 

b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros
*/

let listaCarros = [
    {nome : 'HB20', consumo: 15},
    {nome : 'Ferrari', consumo: 5},
    {nome : 'Onix', consumo: 12},
    {nome : 'corola', consumo: 10},
    {nome : 'Civic', consumo: 9}
]

function verifyCar(listCarros) {
    let maisEconomico = listCarros.reduce((a, b) => (a.consumo < b.consumo) ? b : a)
    return `O carro mais economico é ${maisEconomico.nome}, fazendo ${maisEconomico.consumo} por litro`
}

let percorrer1km = carro => {
    nom = carro.nome
    cons = 1000 / carro.consumo
    return `O carro ${nom} gasta ${cons} litros de gasolina para percorrer 1000km`
}
console.log(verifyCar(listaCarros))
console.log(listaCarros.map(percorrer1km))
