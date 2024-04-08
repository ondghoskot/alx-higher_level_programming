#!/usr/bin/node

function factorial (a) {
  let f = 1;
  if (isNaN(a) || Number(a) === 0) {
    return f;
  } else {
    f = Number(a) * factorial(Number(a) - 1);
    return f;
  }
}

const cla = process.argv[2];
const result = factorial(cla);

console.log(result);
