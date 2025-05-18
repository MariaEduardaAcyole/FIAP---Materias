async function carregar() {
    const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products');
    const dados = await res.json();
    const ul = document.getElementById("produtos");
    ul.innerHTML = "";

    // Parte do carregamento de produtos:
    dados.forEach(p => {
        const li = document.createElement("li");
        const btn = document.createElement("button");
        btn.textContent = "Excluir";
        btn.onclick = async () => {
            await fetch(`https://66429d3a3d66a67b3437cdb2.mockapi.io/products/${p.id}`, {
                method: 'DELETE'
            });
            li.remove();
        };
        li.innerHTML = `
        <img src="${p.image}" alt="${p.name}" style="width: 100px;"><br>
        ${p.name} - R$${p.price}
    `;
        li.appendChild(btn);
        ul.appendChild(li);
    });

}
carregar();

document.getElementById('form').onsubmit = async (e) => {
    e.preventDefault();
    const produto = {
        name: nome.value,
        price: parseFloat(preco.value),
        image: imagem.value,
        seller: "Usuário"
    };
    await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(produto)
    });
    await carregar(); // <-- aqui!
    alert("Produto criado!");
    console.table(dados);

};

