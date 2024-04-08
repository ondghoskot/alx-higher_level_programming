#!/usr/bin/node

const cla = process.argv[2];
let MyNumber = Number(cla);
if (!isNaN(MyNumber) && typeof MyNumber === "number") {
  MyNumber = Math.floor(MyNumber);
  console.log(`My number: ${MyNumber}`);
} else {
  console.log("Not a number");
}
