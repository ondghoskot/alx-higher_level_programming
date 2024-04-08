#!/usr/bin/node

const cla = process.argv[2];
const size = Number(cla);

if (!isNaN(cla)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  } else {
    process.exit(1);
  }
} else {
  console.log('Missing size');
}
