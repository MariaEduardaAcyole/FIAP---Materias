// Criação de objeto usando sintaxe literal
const tarefa = {
    id: 1,
    titulo: "Aprender sobre objetos",
    descricao: "Estudar propriedades e métodos",
    concluida: false,
    prioridade: "alta",
    dataCriacao: new Date()
};
console.log("Objeto tarefa:", tarefa);
console.log("Título (ponto):", tarefa.titulo);
console.log("Prioridade (colchetes):", tarefa["prioridade"]);

// Objeto com nomes especiais (acessados com colchetes)
const tarefaEspecial = {
    "nome da tarefa": "Tarefa com espaço",
    "data-criacao": "2025-01-01"
};
console.log("Nome especial:", tarefaEspecial["nome da tarefa"]);
const projetoTaskMaster = {
    nome: "TaskMaster",
    version: "1.0",
    autor: "Curso JavaScript",
    tarefas: [],
    adicionarTarefa(titulo, prioridade = "média") {
        const novaTarefa = {
            id: this.tarefas.length + 1,
            titulo,
            prioridade,
            concluida: false,
            criada: new Date()
        };
        this.tarefas.push(novaTarefa);
        console.log(`Tarefa "${titulo}" adicionada.`);
        return novaTarefa;
    },
    listarTarefas() {
        console.log(`Projeto ${this.nome} - Lista de Tarefas:`);
        this.tarefas.forEach(t => console.log(`- ${t.id}: ${t.titulo} (${t.prioridade})`));
    }
};

projetoTaskMaster.adicionarTarefa("Estudar Objetos", "alta");
projetoTaskMaster.adicionarTarefa("Criar interface");
projetoTaskMaster.listarTarefas();

// Iterando com for...in
console.log("Propriedades do objeto tarefa:");
for (let prop in tarefa) {
    console.log(`${prop}: ${tarefa[prop]}`);
}

// Object.keys e Object.values
console.log("Chaves:", Object.keys(tarefa));
console.log("Valores:", Object.values(tarefa));

console.log(projetoTaskMaster)

const prioridades = ["baixa", "media", "alta"]
const [baixa,... outrasPrioridades] = prioridades

console.log(baixa)
console.log(outrasPrioridades)

const tarefa1 = {
    id: 1,
    nome: "estudar js",
    data: new Date(
    )
}

