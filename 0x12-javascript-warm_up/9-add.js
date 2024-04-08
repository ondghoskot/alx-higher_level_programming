#!/usr/bin/node

function add(a, b) {
  return Number(a) + Number(b);
}

const first = process.argv[2];
const second = process.argv[3];

result = add(first, second);
console.log(result);
