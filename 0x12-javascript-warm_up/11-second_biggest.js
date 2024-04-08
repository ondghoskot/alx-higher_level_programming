#!/usr/bin/node

const len = process.argv.length;
if (len > 3) {
  let max = Number(process.argv[2]);
  for (let i = 3; i < len; i++) {
    const Num = Number(process.argv[i]);
    if (!isNaN(Num) && max < Num) {
      max = Num;
    }
  }
  console.log(max);
} else {
  console.log(0);
}
