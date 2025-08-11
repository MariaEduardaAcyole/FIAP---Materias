'use client'
import "../app/style.css";

export default function Button({ativo, clicar}) {
 
  return (
      <button className={ativo ? "btn active" : "btn inactive"}
      onClick={clicar}
      >
        Clique aqui
      </button>
  );
}
