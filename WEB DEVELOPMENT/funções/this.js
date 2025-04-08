// Demonstração de "this" em função tradicional vs. arrow function
const contador = {
    valor: 0,
    incrementarTradicional: function () {
        setTimeout(function () {
            // Neste caso, "this" não se refere ao objeto "contador"
            console.log("Valor (tradicional):", this.valor);
        }, 1000); //1000 depois de um segundo execute
    },
    incrementarArrow: function () {
        setTimeout(() => {
            // A arrow function preserva o contexto do objeto "contador"
            this.valor++;
            console.log("Valor (arrow):", this.valor);
        }, 100);
    }
};
contador.incrementarTradicional();
contador.incrementarArrow();

//this acessa o escopo da variavel (tipo acessar uma variavel filho daquela funçao/objeto)

function filtrarTarefas (tarefas, callback){
    return tarefas.filter(callback)
}

const tarefas = [
    {id: 1, titulo: 'estudar js', concluida: false },
    {id: 2, titulo: 'estudar js', concluida: true }
]
const pendentes = filtrarTarefas(tarefas, t => !t.concluida)
const concluidas = filtrarTarefas(tarefas, t => t.concluida)

console.log('tarefas pendentes', pendentes)
console.log('tarefas concluidas', concluidas)

