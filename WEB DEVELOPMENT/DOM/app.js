// Seletores de Elementos

// getElementById('id') 
// getElementsByClassName('classe') 
// getElementsByTagName('tag')
// querySelector('seletor') 
// querySelectorAll('seletor') 

// Altera o texto interno
const titulo = document.querySelector('h1');
titulo.textContent = 'Novo Título';

const div = document.querySelector('#container');
div.innerHTML = '<h2> Novo parágrafo com HTML </h2>';

//altera o atributo 
const imagem = document.querySelector('img')
imagem.setAttribute('src', 'image.png')
imagem.setAttribute('width', '200')
imagem.setAttribute('height', '200')
imagem.setAttribute('alt', 'avatar profile')

const caixa = document.querySelector('.box')
caixa.style.backgroundColor = 'red'
caixa.style.width = '200px'
caixa.style.height = '200px'

const botao = document.getElementById('toggleVisibilidade')
botao.addEventListener('click', () => {
    caixa.classList.toggle('bg-azul') //adiciona a classe oculta
})

// const novoItem = document.createElement('li');
// novoItem.textContent = 'Novo item';
// document.querySelector('ul').appendChild(novoItem);

const botao2 = document.getElementById('toggleNovoitem')
botao2.addEventListener('click', () => {
    const novoItem = document.createElement('li');
    novoItem.textContent = 'Novo item';
    document.querySelector('ul').appendChild(novoItem);
})

localStorage.setItem('nome', 'duda')
localStorage.getItem('linguagem', 'js')

const linguagem = localStorage.getItem('linguagem', 'js')

localStorage.removeItem('nome')
console.log(linguagem)

const usuario = { nome: 'duda', idade: 32 }
localStorage.setItem('usuario', JSON.stringify(usuario)) //converte para string no formato de json

const usuarioRecuperado = JSON.parse(localStorage.getItem('usuario'));
console.log(usuarioRecuperado.nome);
console.log(usuarioRecuperado);

// Array para tarefas
let tarefas = JSON.parse(localStorage.getItem("tarefas")) || []; //ou um array preenchido ou um array vazio

// Função para renderizar lista
function renderizarTarefas () {
    const lista = document.getElementById("lista-tarefas"); //pega a lista ordenada do hmtl
    
    lista.innerHTML = "";

    tarefas.forEach((t, i) => {
        const li = document.createElement("li");
        li.textContent = t;
        lista.appendChild(li);
    })
}
//t = elemento 
//i =  indice
renderizarTarefas();

document.getElementById("form-tarefa").onsubmit = (e) => {
    e.preventDefault();
    const input = document.getElementById("input-tarefa");
    tarefas.push(input.value);
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
    input.value = "";
    renderizarTarefas();
};

document.getElementById("btn-limpar").onclick = () => {
    tarefas = [];
    localStorage.removeItem("tarefas");
    renderizarTarefas();
};
