#!/usr/bin/node

const len = process.argv.length;
if (len > 3) {
  let max = Number(process.argv[2]);
  let SecondMax = Number(process.argv[2]);
  for (let i = 3; i < len; i++) {
    const Num = Number(process.argv[i]);
    if (max < Num) {
      max = Num;
    }
  }
  for (let j = 3; j < len; j++) {
    const SecondNum = Number(process.argv[j]);
    if (SecondNum > SecondMax && SecondNum < max) {
      SecondMax = SecondNum;
    }
  }
  console.log(SecondMax);
} else {
  console.log(0);
}
