/*5. Dada a pontuação de alergia de uma pessoa, determine se ela é ou não alérgica a um determinado item e sua lista completa de alergias. 

Um teste de alergia produz uma pontuação numérica única que contém as informações sobre todas as alergias que a pessoa tem (para as quais foi testada). 

A lista de itens (e seus valores) testados são: 
● ovos (1) 
● amendoim (2) 
● marisco (4) 
● morangos (8) 
● tomates (16) 
● chocolate (32) 
● pólen (64) 
● gatos (128) 

Portanto, se Tom é alérgico a amendoim e chocolate, ele recebe uma pontuação de 34. Agora, dada a pontuação de 34, seu programa deve ser capaz de dizer: 

Se Tom é alérgico a algum dos alergênicos listados acima. Todos os alergênicos aos quais Tom é alérgico. 

Observação: uma determinada pontuação pode incluir alergênicos não listados acima (ou seja, alergênicos com pontuação de 256, 512, 1024, etc.). Seu programa deve ignorar esses componentes da pontuação. Por exemplo, se a pontuação de alergia for 257, seu programa deve relatar apenas a alergia a ovos (1). 
*/

const alergico = ['ovos', 'amendoin','marisco','morango','tomate','chocolate','polén','gatos']
let result = 0

function descobrirAlergia(list){
    let pontAlergico = 0
    for (i in list){
        if(list[i] == 'ovos'){
        pontAlergico +=1
        }
        else if(list[i] == 'amendoin'){
            pontAlergico +=2
        }
        else if(list[i] == 'amendoin'){
            pontAlergico +=4
        }
        else if(list[i] == 'amendoin'){
            pontAlergico +=8
        }
        else if(list[i] == 'amendoin'){
            pontAlergico +=16
        }
        else if(list[i] == 'amendoin'){
            pontAlergico +=32
        }
    }
}

console.log(descobrirAlergia(alergico))

//switch (alergico) {
//  case 'ovos':  
//    result += 1
//    break
//  case 'amendoin':
//    result += 2;
//    break
//  case 'marisco':
//    result +=4;
//    break
//  case 'morango':
//    result = +8;
//    break
//  default:
//    result = 0;
//}
//
//console.log(result);//