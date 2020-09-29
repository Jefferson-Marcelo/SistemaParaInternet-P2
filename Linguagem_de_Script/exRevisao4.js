notas = [
  {aluno: 'Fulano', nota: 6.5},
  {aluno: 'Ciclano', nota: 8.5},
  {aluno: 'chico', nota: 7.5},
  {aluno: 'José', nota: 9.5},
  {aluno: 'João', nota: 3.5}
]

let aprovados = aprovado => aprovado.nota >= 7.0

let passou = notas
.filter(aprovados)

console.log(passou)