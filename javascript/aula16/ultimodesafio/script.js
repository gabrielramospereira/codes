var num = document.getElementById('snum')
var lista = document.getElementById('slista')
var res = document.getElementById('res')
//var lista = document.querySelector('select#slista')
//var num = document.querySelector('input#snum')
//var res = document.querySelector('div#res')
var valores = []

function isNumero(n){
    if (Number(n)>=1 && Number(n)<=100){
        return true
    }else{
        return false
    }
}

function inLista(n,l){
    if (l.indexOf(Number(n))!= -1){
        return true
    } else{
        return false
    }
}

function adicionar(){
    if(isNumero(num.value) && !inLista(num.value,valores)){   //exclamacao eh negacao
        valores.push(Number(num.value))
        var item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        lista.appendChild(item) // cria um elemento filho option dentro de lista que é um select
        res.innerHTML='' //limpa o resultado, pois estou adicionando um novo option, in other words, um novo numero
    } else{
        window.alert('Valor inválido ou já encontrado na lista.')
    }
    num.value = ''
    num.focus() // o cursor piscar dentro da caixa
}

function finalizar(){
    if(valores.length == 0){
        alert('Adicione valores antes de finalizar.')
    }else{
        var total = valores.length
        var maior = valores[0]
        var menor = valores[0]
        var soma = 0
        var media = 0
        for (c in valores){
            soma+=valores[c]
            if(valores[c]> maior){
                maior = valores[c]
            }
            if(valores[c]< menor){
                menor = valores[c]
            }
        }
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${total} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p>A soma vale ${soma} e a média vale ${soma/valores.length}.</p>`
    }
}

