function tabuada(){
    var num = document.getElementById('txtn')
    var tab = document.getElementById('selTab')
    if(num.value.length == 0){
        alert('Digite um número!')
    } else{
        var n = Number(num.value)
    }
    tab.innerHTML=''
    var c=1
    while(c<=10){
        var item = document.createElement('option')   // criando um option dentro de um select de forma dinamica
        item.text = `${n} x ${c} = ${n*c}`
        item.value = `tab${c}`
        tab.appendChild(item)
        c++
    }
}