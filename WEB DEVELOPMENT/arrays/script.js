console.log("Hello World")
const tarefas = [
    "Estudar Js",
    "Criar projeto",
    "Preparar apresentação",
    "Revisar Código"
]
console.table(tarefas)

const categorias = new Array("Trabalho", "Estudo", "Pessoal", "Projetos")
console.table(categorias)

const prioidades = Array.of("Baixa", "Media", "Alta")
console.table(prioidades)

const letras = Array.from('Daniel') //separa as letras
console.table(letras)

console.log(letras[1]) //acessar uma letra especifica

const outrasTarefas = [
    "Estudar Js",
    "Ciar projeto",
    "Preparar apresentação",
    "Revisar Código"
]

console.table(outrasTarefas[outrasTarefas.length - 1]) //imprimir o ultimo elemento
// porque lenght é o ultimo assim que subtrai um passa a ser o ultimo

outrasTarefas[2] = "power point" //altera o indice 2
console.log(outrasTarefas)

outrasTarefas.push("realizar testes") //add
console.log(outrasTarefas)

outrasTarefas.unshift("preparar ambietes") //
console.log(outrasTarefas)

outrasTarefas.shift()
console.log(outrasTarefas)

outrasTarefas.pop()
console.log(outrasTarefas)

outrasTarefas.splice(2, 1) //remove indice 2
outrasTarefas.splice(2, 0, "Realizar testes") //adiciona no indice 2
outrasTarefas.splice(2, 1, "Preparar apresentação") //altera o valor

console.log(outrasTarefas)

// callback é uma função passada como parametro de outra função
// callback é uma função anonima
// no caso do forEach pode usar uma função declarada
// forEach espera dois parametros


// tarefas.forEach(callback);
// tarefas.forEach((elemento, idx) => {

// });

tarefas.forEach = (el, idx) => {
    console.log(`${idx + 1}. ${el}`)
}

const tarefasModificado = tarefas.map(el => el.toUpperCase())
console.log(tarefasModificado)
tarefasModificado.push("teste")
console.log(tarefas)


const tarefasComA = tarefas.filter(el => el.includes("p"))
console.log(tarefasComA) // varios elementos retornados


const tarefasComA2 = tarefas.find(el => el.includes("p"))
console.log(tarefasComA2) // retorna apenas um

const tarefasComA3 = tarefas.findIndex(el => el.includes("Js"))
console.log(tarefasComA3) // retorna o index do elemento

tarefas.splice(tarefasComA3, 1) //deletou
console.log(tarefas)

const valorProdutos = [10, 56, 88]
const somaComprimentos = valorProdutos.reduce((total, t) => total + t, 0)
// quantidade de caacteres total de uma string
console.log(somaComprimentos)

const atv = {
    id: 1,
    titulo: "aprender sobre objetos",
    descricao: "estudar propriedades",
    concluida: false,
    prioidade: "alta",
    dataCriacao: new Date()
}

console.log(atv)
console.log(atv.titulo)
console.log(atv["titulo"])
console.log(atv?.titulo)

const tarefaEspecial = {
    "nome da tarefa": "tarefa com espaço",
    "data-cricao": "tarefa com traco"
}


console.log(tarefaEspecial['nome da tarefa'])
console.log(tarefaEspecial['data-cricao'])
