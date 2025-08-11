'use client'
import { useState } from 'react';
import "../app/style.css";
import Button from "./button.js";

const Titulo = ({ texto }) => <h1>{texto}</h1>;

const Subtitulo = ({ texto }) => {
  return (
    <>
      <h2>{texto}</h2>
    </>
  );
};

const Alerta = ({ tipo = 'info', children, ...rest }) => {
  const classe = `alert ${tipo}`;
  return (
    <div className={classe} {...rest}>
      {children}
    </div>
  );
};

const itens = ['React', 'Vue', 'Angular'];
const cursos = [{ id: 101, turma: '1ESS' }];

export default function Home() {
  const [active, setActive] = useState(true);

  return (
    <>
      <Titulo texto="Esse é o texto no componente Titulo" />
      <Subtitulo texto="Esse é o componente de Subtítulo" />
      
      <Button ativo={false} />
      <Button ativo={true} />
      <Button ativo={active} onClick={() => setActive(!active)} />

      <ul>
        {itens.map(framework => (
          <li key={framework}>{framework}</li>
        ))}
        {
        cursos.map(c => (
          <li key={c.id}>{c.turma}</li>
        ))}
      </ul>

      <Alerta id="alerta">
        <h1>ALERTA</h1>
      </Alerta>
    </>
  );
}

  // // // não pode retornar dois elementos //<></> usar tag vazia se precisar
  //   // <>
  //   //   <div>Esta é a minha página</div>
  //   //   <h1 className="classe-do-h1">Soma= {soma}</h1>
  //   //   {/*Esse é um comentario dentro de um JSX*/}
  //   //   {console.log("Essa é a soma exibida no console:", soma)}
  //   // </>
  //   <>
  //     {/* {
  //     pontos > 0 ? 'Voce tem pontos' : 'voce NAO tem pontos'
  //   }  */}