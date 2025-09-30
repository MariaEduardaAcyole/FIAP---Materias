// src/App.jsx
import ThreeColumnHero from "./components/ThreeColumnHero";
import DecoratedText from "./components/DecoratedText";
import FloatedImageArticle from "./components/FloatedImageArticle";
import OverlaySVG from "./components/OverlaySVG";
import Tipografia from "./components/Tipografia";
import GalleryHybrid from "./components/GalleryHybrid";

function App() {
  return (
    <div className="space-y-12">
      <ThreeColumnHero />
      <DecoratedText />
      <FloatedImageArticle />
      <OverlaySVG />
 
      <Tipografia />
      <GalleryHybrid />
    </div>
  );
}

export default App;