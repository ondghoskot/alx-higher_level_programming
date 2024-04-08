#!/usr/bin/node

let count = 0;

for (const argv of process.argv) {
  count++;
} 
if (count <= 2) {
  console.log('No argument');
} else {
  const cla = process.argv.slice(2,3);
  arg = cla.toString();
  console.log(arg)
}
