numeros = [0,1,2,3,4,5,6]
novaLista = []
const somador = function(acc,ele) {  
  novaLista.push(acc+ele)
  return acc + ele
}
let soma = numeros.reduce((somador),0)
console.log(novaLista)
