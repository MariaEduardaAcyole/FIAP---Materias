console.log('Hello World')

//operador

let idade = 18
let resultado = idade >= 18 ? "maior de idade" : "menor de idade"
console.log(resultado)

//coalescencia nula

let valor = null;
let res = valor ?? "valor padrao"
console.log(res)

//encadeamento opcional

let usuario = {
    nome: 'duda'
}

console.log(usuario?.idade) //indica que é opcional estar preenchido o campo idade

//arrays

//operador spreed

let arr1 = [1, 2]
let arr2 = [3, 4]

console.log(arr1, arr2)

let combinadodosdoisarrys = [...arr1, ...arr2]
console.log(combinadodosdoisarrys)

//if / else

let tarefaConcluida = true

if (tarefaConcluida) {
    console.log('ta conluida')
}

else {
    console.log('nao ta concluida')
}


let prioridade = 2
if (prioridade === 1) {
    console.log('prioridade baixa')
}

else if (prioridade === 2) {
    console.log('prioridade media')
}

else if (prioridade === 5) {
    console.log('prioridade alta')
}

else {
    console.log('prioridade desconhecida')
}

//switch case

let diaSemana = new Date('04-01-2025').getDay()
console.log('hoje é', diaSemana)

switch (diaSemana) {
    case 0:
        console.log('domingo')
        break;
    case 1:
        console.log('Segunda')
        break;
    case 2:
        console.log('terça')
        break;
    case 3:
        console.log('Quarta')
        break;
    case 4:
        console.log('Quinta')
        break;
    case 5:
        console.log('Sexta')
        break;
    case 6:
        console.log('Sabado')
        break;
    default:
        console.log('dia invalido')
        break;
}

//for

for (let i = 0; i <= 5; i++) {
    console.log('FOR: ', i)
}

//while

let i = 0
while(i<=5){
    console.log('WHILE: ', i)
    i++
}

//

let c = 0;
do {
    console.log('DO WHILE:',c)
    c++
} while( c < 5)