//tipos de funções

// #expressao de função - melhor forma porque gera erro explicito
const nomedafuncao = function () { }

// A função "saudar" é declarada e sofre hoisting.
console.log(saudar('daniel'))
function saudar(nome) {
    // Retorna uma mensagem personalizada
    return `Olá, ${nome}! Bem-vindo ao TaskMaster.`; //Ouput = Olá, daniel! Bem-vindo ao TaskMaster.
}

console.log(nome) //output = undeffined
var nome = 'duda'

// JEITO UIM COM ERO AO NAO DAR MAIS DE UM PARAMETRO
function criarTarefa(titulo, descricao,
    prioridade, concluida) {
    return {
        id: Date.now(), // Gera um ID único com base no timestamp
        titulo,
        descricao,
        prioridade,
        concluida,
        criada: new Date()
    };
}
// const tarefa = criarTarefa("Estudar funções"); //vira o titulo
// console.log(tarefa);

// -----------------------

function criarTarefa(titulo, descricao,
    prioridade, concluida) {
    if (!titulo || !descricao || !prioridade || concluida) {
        console.error('voce precisa informar todos os parametros')
        return false
    }
    return {
        id: Date.now(), // Gera um ID único com base no timestamp
        titulo,
        descricao,
        prioridade,
        concluida,
        criada: new Date()
    };
}

const tarefa = criarTarefa("Estudar funções"); //vira o titulo
console.log(tarefa);

