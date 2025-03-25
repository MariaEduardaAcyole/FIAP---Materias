// Métodos básicos
console.log("Mensagem normal");
console.info("Informação");
console.warn("Aviso"); //fica em vermelho mas nao necessariamente tem erro 
console.error("Erro"); //quando de fato tem erro 

// Tabelas
console.table([
    { id: 1, tarefa: "Estudar JS" },
    { id: 2, tarefa: "Praticar código" }
]);

// Agrupamento
console.group("Grupo de logs"); //agrupa o log
console.log("Log 1");
console.log("Log 2");
console.groupEnd();

// Medição de tempo
console.time("Timer");
// ...algum processamento...

var antigo = 'forma antiga de declarar variaveis'
let oLet = 'permite mudar o valor da variavel com outro valor no bloco acima'
const Oconst = 'imutavel'

console.log(Oconst)
console.log(oLet)
console.log(antigo)

console.timeEnd("Timer");


//tipos de dados primitivos
console.log('\n TIPO DE DADOS PRIMITIVOS')
let texto = "Olá";
console.log(texto)

let numero = 42;
console.log(numero)

let isCompleted = false;
console.log(isCompleted)

let semValor; //undefined
console.log(semValor)

let nulo = null;
console.log(nulo)

let uniqueId = Symbol("id");
console.log(uniqueId)

let bigNumero = 999999999999999999999999n;
console.log(bigNumero)

console.log('\n SEUS TIPOS DE DADOS PRIMITIVOS')

console.log(typeof texto); // "string"
console.log(typeof numero); // "number"
console.log(typeof isCompleted); // "boolean"
console.log(typeof semValor); // "undefined"
console.log(typeof nulo); // "object" (bug conhecido do JS)
console.log(typeof uniqueId); // "symbol"
console.log(typeof bigNumero); // "bigint"

let tasks = [
    { id: '1', descricao: 'tarefa 01' }, //->objetos
    { id: '2', descricao: 'tarefa 02' }
]
console.log(tasks)
console.log(tasks[0]['id']) //1

let hoje = new Date()
console.log(hoje)
let futuro = new Date("03-25-2025") //mes-dia-ano
console.log(futuro)

let pattern = /^[a-z]+$/i //tem letra de A a Z
console.log(pattern.test("javascript"))

let troca = 'oi'

console.log(typeof (troca))
console.log(typeof parseInt(troca))
console.log(typeof parseFloat(troca))

let textopreenchido = 'texto'
let textovazio = ''

console.log(Boolean(textopreenchido))
console.log(Boolean(textovazio))


//Operadores Aritméticos (+, -, *, /, %, **)
console.log('=== Operadores Aritméticos (+, -, *, /, %, **) ===')
let a = 10;
let b = 3;
console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.333...
console.log(a % b); // 1
console.log(a ** b); // 1000


// Operadores de Incremento/Decremento (++, --)

let contador = 0;
let contador2 = 0;

console.log(contador)
console.log(contador++); // 1 (pós-incremento, agora contador = 2)
console.log(contador)
console.log(contador2)
console.log(++contador2); // 1 (pré-incremento)

//Operadores de Atribuição (=, +=, -=, *=, /=, %=, **=)
console.log('Operadores de Atribuição (=, +=, -=, *=, /=, %=, **=)')
let x = 10;
x += 5; // x = 15
x -= 3; // x = 12
x *= 2; // x = 24
x /= 4; // x = 6
x %= 2; // x = 0
x **= 3; // x = 0 (0 elevado a 3)

//Operadores de Comparação(==, ===, !=, !==, >, <, >=, <=)
console.log('Operadores de Comparação(==, ===, !=, !==, >, <, >=, <=)')

console.log(10 == "10");   // true (compara valor somente)
console.log(10 === "10");  // false (compara valor e tipo)
console.log(5 != "5");     // false (valor é igual)
console.log(5 !== "6");    // true (valor igual, mas tipo diferente)

//Operadores Lógicos(&&, ||, !)
console.log('Operadores Lógicos(&&, ||, !)')

console.log(true && false);  // false (AND)
console.log(1 === 1 && 1 == 2)

console.log(true || false);  // true  (OR)
console.log(1 === 1 || 1 == 2)

console.log('------')
console.log(!true);// false (NOT)
console.log(!(1 == 1))// false
console.log(!(1 == 2))//true
