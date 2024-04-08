#!/usr/bin/node

const len = process.argv.length;
if (len > 3) {
  let max = process.argv[2];
  for (let i = 3; i < len; i++) {
    if (max < process.argv[i]) {
      max = process.argv[i];
    }
  }
  console.log(max);
} else {
  console.log('0');
}
