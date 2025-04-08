function fatorial(n) {
    if (n === 0 || n === 1) return 1;  // Caso base
    console.log("exiba o valor atual de n:", n);
    return n * fatorial(n - 1);        // Chamada recursiva
  }
  console.log("Fatorial de 5:", fatorial(5));