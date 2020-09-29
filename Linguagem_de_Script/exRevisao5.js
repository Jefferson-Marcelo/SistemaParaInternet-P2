function intervalo(x,y){  
  lista = []
  for (let i=x+1; i<y; i++){
    lista.push(i)
  }
  return lista
}

console.log(intervalo(2,9))