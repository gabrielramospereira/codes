function carregar(){
var msg = document.getElementById('msg')
var img = document.getElementById('imagem')
var data = new Date()
var hora = data.getHours()
msg.innerText = `Agora são ${hora} horas.`
if (hora>0 && hora < 12){
    img.src = 'fotomanha.png'
    document.body.style.background = '#e2cd9f'
} else if(hora<=18){
    img.src = 'fototard.png'
    document.body.style.background = '#b9846f'
}else{
    img.src = 'fotonoite.png'
    document.body.style.background = '#515154'
}
}