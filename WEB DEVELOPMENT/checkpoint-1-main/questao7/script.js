
let a = true;
let b = false;

let x = 1;
let y = 0;



console.log(a && b); // false (true AND false)
console.log(a && a); // true (true AND true)

console.log(x && y); // 0 (1 AND 0 - false)
console.log(x && x); // 1 (1 AND 1 - True)


console.log(a || b); // true (true OR false)
console.log(a || a); // true (true OR true)


console.log(!a); // false (NOT true)
console.log(!b); // true (NOT false)
