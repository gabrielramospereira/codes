/*function parimpar(n){   //parimpar
    if(n%2 ==0){
        return 'par'
    }else{
        return 'impar'
    }
}
var res = parimpar(5)
console.log(res)

function soma(n1=0,n2=0){   //soma
    return n1+n2
}

console.log(soma(2,3))

function fatorial (n){   //fatorial
    var fat = 1
    for (c=n;c>1;c--){
        fat=fat*c
    }
    return fat
}
console.log(fatorial(5))*/

function fatorial(n){  // recursão
    if (n==1){
        return 1
    } else{
        return n*fatorial(n-1)
    }
}
console.log(fatorial(5))

