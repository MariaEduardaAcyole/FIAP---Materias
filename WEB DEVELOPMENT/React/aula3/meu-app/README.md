This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
```

# Teoria

## ESTADO

Estado é o conjunto de dados que **representa a situação atual de um componente**. Quando o estado muda, o React re-renderiza o componente exibindo os novos valores.

- Estado vive dentro do componente (não é global).
- O React compara a nova árvore de JSX e atualiza a tela de forma eficiente.
- Estados diferentes ⇒ renderizações diferentes.

**Dica mental**: pense no JSX como uma função do estado: UI = f(estado)

## HOOKS 

Hooks são funções especiais do React que permitem **“ligar” recursos da biblioteca em componentes funcionais**. Substituiu o class components.

SERVE PARA: Foram introduzidos no React 16.8 para simplificar e unificar a forma de escrever componentes.
- Permitem usar estado, efeitos colaterais e outras funcionalidades sem precisar de classes.
- Sempre começam com a palavra use (ex: useState, useEffect, useContext).

**Dica mental**: Hooks são como “atalhos” para acessar recursos avançados do React em componentes funcionais.


Cria a variavel x com valor dinamico e quando muda o estado passa a alterar em setX
**Hook sempre no inicio**

```
// ✅ Correto
export default function Exemplo() {
  const [x, setX] = useState(0);
  // ...
  return <div />;
}

// ❌ Errado (hook dentro de condicional)
export default function Erro() {
  if (Math.random() > 0.5) {
    const [x, setX] = useState(0); // NÃO FAÇA ISSO
  }
  return <div />;
}
```
## USE STATE
```
import { useState } from 'react';

export default function Contador() {
  const [valor, setValor] = useState(0);

  function incrementar() {
    setValor(valor + 1); // atualização baseada no valor atual
  }

  return (
    <div>
      <p>Valor: {valor}</p>
      <button onClick={incrementar}>Adicionar</button>
    </div>
  );
}
```

### Atualização funcional (evita “estado antigo”)
Quando a nova atualização depende do estado anterior, use a forma funcional:
**ele sabe que tem que pegar de x porque esta linkado no setvalor que ta linkado a x**

```
const[x,setvalor] = use

setValor(prev => prev + 1); // seguro mesmo com várias atualizações seguidas
```

- Expredi operator é o mesmo que pegar o conteudo de um balde e passar para outro balde, nao é copiar

### Objetos e arrays no estado (imutabilidade)
Não modifique direto. Crie uma nova cópia ao atualizar.
```
const [aluno, setAluno] = useState({ nome: 'Ana', pontos: 0 });

// ❌ NÃO faça:
// aluno.pontos = aluno.pontos + 1; setAluno(aluno);

// pontos variavel que eu quero
// prev.pontos o valor anterior de pontos

// ✅ Faça:
setAluno(prev => ({ ...prev, pontos: prev.pontos + 1 }));

const [lista, setLista] = useState(['A', 'B']);
setLista(prev => [...prev, 'C']); // adiciona sem mutar

//prev é uma função
// ...prev é oque eu pego do objeto (conteudo)
// pontos a variavel que sera alterada 

```

### Inputs controlados (estado <→ input)
```
function FormNome() {
  const [nome, setNome] = useState('');

  return (
    <div>
      <input value={nome} onChange={e => setNome(e.target.value)} placeholder="Seu nome" />
      //toda vez que o evento dentro do input é acionado = pega valor do input
      
      <p>Olá, {nome || 'Visitante'}!</p>

    </div>
  );
}
```

## useEffect

useEffect executa efeitos colaterais: chamar APIs, configurar timers, listeners, sincronizar com armazenamento, etc. A assinatura é ```useEffect(callback, deps?)```.

### Padrões de dependência

- Sem array: roda em toda renderização (cuidado!).
- Array vazio []: roda uma vez no mount e limpa no unmount.
- [x, y]: roda quando x ou y mudarem.

```
import { useState, useEffect } from 'react';

export default function Relogio() {
  const [hora, setHora] = useState(new Date());

  useEffect(() => {
    const id = setInterval(() => setHora(new Date()), 1000);
    return () => clearInterval(id); // limpeza no unmount
  }, []); // renderiza uma vez. Se quiser que seja executado toda vez que alterar a variavel tem que por parametros nos []

  return <p>{hora.toLocaleTimeString()}</p>;
}
```

### Exemplo: escutar eventos do teclado (com limpeza)
```
function Teclado() {
  const [ultimaTecla, setUltimaTecla] = useState('');

  useEffect(() => {
    const onKey = (e) => setUltimaTecla(e.key);
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  return <p>Última tecla: {ultimaTecla}</p>;
}
```

### Exemplo: busca em API (com carregando/erro)

```
function Usuarios() {
  const [dados, setDados] = useState([]);
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    let ativo = true;
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(r => r.json())
      .then(json => { if (ativo) { setDados(json); setCarregando(false); }})
      .catch(e => { if (ativo) { setErro(e.message); setCarregando(false); }});
    return () => { ativo = false; };
  }, []);

  if (carregando) return <p>Carregando...</p>;
  if (erro) return <p>Erro: {erro}</p>;

  return (
    <ul>
      {dados.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```
