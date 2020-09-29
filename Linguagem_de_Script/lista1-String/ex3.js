/*3. Fazer um programa de “criptografia” (codificação de dados visando a privacidade de acesso às informações), no qual é dada uma string (vetor de caracteres) para que este programa codifique os dados através de um processo de substituição de letras. Você pode definir o seu próprio método de criptografia, desde que depois seja possível reverter este processo, ou seja, um código criptografado deve poder ser convertido novamente ao valor inicial. 

Exemplo: >> Criptografador – Codifica uma String << Entre como texto (string) a ser criptografado: Linguagem Texto criptografado: MjohvbhfnD 

Dica: Caracteres também permitem operações numéricas como por exemplo: Letra = Letra + 1; Somar 1 ao código de uma letra, implica em transformar esta no caracter seguinte (http://pt.wikipedia.org/wiki/ASCII). 
*/
let nome = 'Jefferson Marcelo'

function Criptografador(nome) {
    let novoNome = nome.split("")
    for (let i = 0; i < novoNome.length; i++) {
        novoNome[i] = novoNome[i].charCodeAt() + 5;
        novoNome[i] = String.fromCharCode(novoNome[i]);
    };
    return novoNome.join("");
};

function desCriptografador(nome) {
    let novoNome = nome.split("")
    for (let i = 0; i < novoNome.length; i++) {
        novoNome[i] = novoNome[i].charCodeAt() - 5;
        novoNome[i] = String.fromCharCode(novoNome[i]);
    };
    return novoNome.join("");
};

nome_criptografado = Criptografador(nome)
descriptografar_nome = desCriptografador(nome_criptografado)

console.log(nome_criptografado);
console.log(descriptografar_nome);