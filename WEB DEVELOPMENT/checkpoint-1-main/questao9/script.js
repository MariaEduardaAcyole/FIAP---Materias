function compararNumeros(a, b) {
    if (a > b) {
         console.log("A é maior");
    } else if (b > a) {
        console.log("B é maior");
    } else {
       console.log("Ambos são iguais");
    }
  }
  
  console.log(compararNumeros(5, 10)); // esperado: "B é maior"
  console.log(compararNumeros(10, 5)); // esperado: "A é maior"
  console.log(compararNumeros(7, 7));  // esperado: "Ambos são iguais"