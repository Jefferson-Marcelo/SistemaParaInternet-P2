let biblioteca = [
    {
    titulo: 'Morte no Nilo',
    autor: 'Agatha Christie',
    bibliotecaID: 1254
    },
    {
    titulo: 'Os miseráveis',
    autor: 'Victor Hugo',
    bibliotecaID: 4264
    },
    {
    titulo: 'O Senhor dos Anéis',
    autor: 'JRR Tolkien',
    bibliotecaID: 3245
    },
    ];
let ordem = biblioteca.sort((a, b) => {
    (a.autor > b.autor) ? 1 :((b.autor > a.autor) ? -1 :0)})      
console.log(ordem)

//let ordenar = livro => `{título : ${livro.titulo}, autor : ${livro.autor}, biblioteca : ${livro.//bibliotecaID}}`
//let transforjson = JSON.stringify(biblioteca.map(ordenar).sort())
//console.log(transforjson)