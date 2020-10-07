let receitaFavorita = {
    titulo: 'Carne Apimentada',
    Porções: 2,
    Ingredientes: [
        'carne',
        'canela',
        'cominho',
        'cacau',
        'pimenta'
    ]
}    

console.log(`${receitaFavorita.titulo}`)
console.log(`${Object.keys(receitaFavorita)[1]} : ${receitaFavorita.Porções}`)
console.log(`${Object.keys(receitaFavorita)[2]} :`) 
for (let i = 0; i < 5; i++) {
    console.log(receitaFavorita.Ingredientes[i])
}
