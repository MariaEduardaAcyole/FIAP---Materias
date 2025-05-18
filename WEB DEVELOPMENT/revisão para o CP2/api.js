
const buscarUsuarios = async () => {
const res = await fetch('https://jsonplaceholder.typicode.com/users')

const dados = await res.json();

    dados.forEach(usuario => {
      console.log(usuario.name);
    });
}

console.log(buscarUsuarios())

// .then()?
// É usado para esperar uma resposta da API (já que a requisição pode demorar).

// resposta.json() 
// converte o que veio da API em um objeto JavaScript legível.

// async	
// Sem isso, não pode usar await

// await	Sem isso, a resposta pode vir "crua" ou incompleta

// buscarUsuarios();	
// Chamar a função, senão nada acontece!