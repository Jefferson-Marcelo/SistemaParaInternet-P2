function calculadoraDeIMC(sexo,peso,altura) {
    const sexoElemento = document.querySelector('input:checked').value
    console.log(sexoElemento)
    const alturaElemento = document.querySelector('input[name=altura]')
    const altura = alturaElemento.value
    //console.log(altura)
    const pesoElemento = document.querySelector('input[name=peso]')
    const peso = pesoElemento.value
    //console.log(peso)
    const imcElemento = document.querySelector('#imc')
    imcElemento.value = imc
    let imc = peso/altura**2

    let sexoMasc = document.querySelector("#masculino")
    let sexoFem = document.querySelector("#feminino")

    if (sexoFem = 'feminino'){
        return imcMulher()
    }
    else if (sexoMasc = 'masculino'){
        return imcHomem()
    } 
    function imcMulher(){
        if (imc < 19.1) return `O imc é ${imc} e você estar abaixo do peso`        
        else if (imc < 25.8) return `O imc é ${imc} e você estar com o peso Normal`        
        else if (imc < 27.3) return `O imc é ${imc} e você estar levemente acima do peso`        
        else if (imc < 32.5) return `O imc é ${imc} e você estar acima do peso ideal`
        else return `O imc é ${imc} e você estar obeso. Vamos nos cuidar por causa do coronga`    
    }
    function imcHomem(){
        if (imc < 20.7) return `O imc é ${imc} e você estar abaixo do peso`        
        else if (imc < 26.4) return `O imc é ${imc} e você estar com o peso Normal`        
        else if (imc < 27.8) return `O imc é ${imc} e você estar levemente acima do peso`        
        else if (imc < 31.1) return `O imc é ${imc} e você estar acima do peso ideal`
        else return `O imc é ${imc} e você estar obeso. Vamos nos cuidar por causa do coronga`    
    }    
    
}
