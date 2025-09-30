// components/Tipografia.jsx
export default function Tipografia() {
  return (
    <div className="p-6 space-y-4">
      <h1 className="text-4xl md:text-5xl font-extrabold">Título Principal</h1>
      <h2 className="text-2xl md:text-3xl font-semibold">Subtítulo</h2>
      <p className="text-gray-700 leading-relaxed">
        Texto corrido com <span className="italic text-blue-600">destaque</span> e variações de peso e cor.
      </p>
      <blockquote className="border-l-4 border-blue-500 pl-4 italic text-gray-600">
        "Exemplo de citação com estilo tipográfico diferenciado."
      </blockquote>
    </div>
  );
}