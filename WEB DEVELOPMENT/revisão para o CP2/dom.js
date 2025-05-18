document.getElementById("meuBotao").addEventListener("click", function() {
  document.getElementById("mensagem").innerText = "Você clicou!";
});

function dataAtualFormatada(){
    let data = new Date(),
        hora  = data.getHours().toString(),
        minuto  = data.getMinutes().toString()  
    return `${hora}h${minuto}`;
}

console.log(dataAtualFormatada());

document.querySelector('#botao-hora').addEventListener('click', 

    function clico (){
        document.querySelector('#paragrafo-hora').innerHTML = dataAtualFormatada(); 
    }
);