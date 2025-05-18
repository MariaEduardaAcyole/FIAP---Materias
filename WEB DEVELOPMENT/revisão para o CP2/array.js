let lista = ['maça', 'banana', 'uva'];
console.log(lista)
lista.pop();  // remove o último

lista.push("morango")  // adiciona no final
console.log(lista.length)
console.log(lista)
lista.shift(); // remove do começo 
lista.unshift("kiwi"); // adiciona no começo

let usuarios = [
    { nome: "João", idade: 20 },
    { nome: "Ana", idade: 25 },
    { nome: "Carlos", idade: 30 }
];

let nomes = usuarios.map(usuario => usuario.nome);
console.log(nomes); // ["João", "Ana", "Carlos"]

// Dado o array de preços abaixo, use map() para retornar um novo array
// com todos os preços com 10% de desconto.

let precos = [100, 200, 300, 400];

let novosPrecos = precos.map(precos => precos - (precos * 0.10))
console.log(novosPrecos)

// Crie um array de 5 números
let numeros = [10, 10, 5, 5]
let i = 0

// Some todos os números e mostre no console
const soma = numeros.reduce((acumulador, atual) => acumulador + atual, i); //0 é Valor inicial do acumulador
console.log(soma)

