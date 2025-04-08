//function normal
const subtrair = function (a, b) {
    return a - b
}

//arrow functions
// const soma = (a,b) => a+b

const soma = (a, b) => {
    let resultado = a + b
    return resultado
}

console.log(subtrair(20, 5))
console.log(soma(20, 5))

//map percorre o array
const dobrados = numeros.map(n => n * 2)
console.log(dobrados)
