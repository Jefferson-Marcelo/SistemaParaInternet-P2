/*4. Dada uma sequência de dígitos, calcule o maior produto para uma substring contínua de dígitos de comprimento n. 
Por exemplo, para a entrada '1027839564', o maior produto para uma série de 3 dígitos é 270 (9 * 5 * 6), e o maior produto para uma série de 5 dígitos é 7560 (7 * 8 * 3 * 9 * 5). 

Observe que essas séries só precisam ocupar posições adjacentes na entrada; os dígitos não precisam ser numericamente consecutivos. 

Para a entrada '73167176531330624919225119674426574742355349194934', o maior produto para uma série de 6 dígitos é 23520. 
*/

let listaNumeros = [];

function produtoSub(numero, tamanho) {
    for (var i = 0; i < numero.length; i++) {
        let acumulador = 1;
        var subString = numero.substr(i, tamanho);
        for (var j = 0; j < subString.length; j++) {
            acumulador *= parseInt(subString[j]);
        };
        listaNumeros.push({subString, acumulador});
    };

    listaNumeros.sort(function (a, b) {
        return (b.acumulador - a.acumulador);
    });

    return `Resultado:\nO maior produto vem da substring '${listaNumeros[0].subString}', equivalendo a ${listaNumeros[0].acumulador}.`;
};

console.log(produtoSub('1027839564', 3));
console.log(produtoSub('1027839564', 5));
console.log(produtoSub('73167176531330624919225119674426574742355349194934', 6));