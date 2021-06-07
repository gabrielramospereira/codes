function contar(){
    var inicio = document.getElementById('txti')
    var passo = document.getElementById('txtp')
    var fim = document.getElementById('txtf')
    var res = document.getElementById('res')

    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0 ){
        alert('Faltam dados!')
        res.innerHTML ='Impossível contar'
    } else{
        res.innerHTML = "Contando: "
        var i = Number(inicio.value)
        var p = Number(passo.value)
        var f = Number(fim.value)
        if(p == 0){
            alert('Passo inválido considerando passo 1')
            p = 1
        }

        if(i<f){
            for(var c=i; c<=f; c+=p){
                res.innerHTML += `${c} \u{1F603} `
            }  
        } else {
            for(var c=i ; c>=f ; c-=p){
                res.innerHTML += `${c} \u{1F603} `
            }
        }
        res.innerHTML += `\u{1F3C1}`

        
    }

}