#!/usr/bin/node

let count = 0;

process.argv.forEach(() => {
  count++;
});
if (count <= 2) {
  console.log('No argument');
} else {
  const cla = process.argv.slice(2, 3);
  const arg = cla.toString();
  console.log(arg);
}
