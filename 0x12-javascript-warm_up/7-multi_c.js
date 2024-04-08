#!/usr/bin/node

const cla = process.argv[2];
const occ = Number(cla);

if (!isNaN(cla)) {
  if (occ > 0) {
    for (let i = 0; i < occ; i++) {
      console.log('C is fun');
    }
  } else {
    process.exit(1);
  }
} else {
  console.log('Missing number of occurrences');
}
