
async function listarProdutos() {
  const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products');
  const produtos = await res.json();
  const ul = document.getElementById("lista-produtos");
  ul.innerHTML = "";

  produtos.forEach(p => {
    const li = document.createElement("li");
    li.innerHTML = `
      <img src="${p.image}" width="50">
      <strong>${p.name}</strong> - R$ ${p.price} <em>(${p.seller})</em>
    `;
    ul.appendChild(li);
  });
}

listarProdutos();

document.getElementById("btn-buscar").onclick = function () {
  const username = document.getElementById("input-usuario").value.trim();
  const info = document.getElementById("info-usuario");
  if (!username) {
    info.innerHTML = "<span style='color:red'>Digite um usuário!</span>";
    return;
  }
  info.innerHTML = "Carregando...";
  fetch(`https://api.github.com/users/${username}`)
    .then(res => {
      if (!res.ok) throw new Error("Usuário não encontrado");
      return res.json();
    })
    .then(data => {
      info.innerHTML = `
        <p><strong>Nome:</strong> ${data.name || "(sem nome)"}</p>
        <img src="${data.avatar_url}" width="100" />
        <p><strong>Repositórios públicos:</strong> ${data.public_repos}</p>
      `;
    })
    .catch(() => {
      info.innerHTML = "<span style='color:red'>Usuário não encontrado!</span>";
    });
};