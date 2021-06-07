var num = [3,5,8,4,0]
num.push(1)
num.sort()
console.log(`O tamanho do vetor é ${num.length}`)
console.log(num)

/*for(var c=0;c<num.length;c++){
    console.log(num[c])
}*/

for(var c in num){
    console.log(num[c])
}
