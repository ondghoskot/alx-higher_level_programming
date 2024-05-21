#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const writeString = process.argv[3];
fs.writeFile(filePath, writeString, 'utf8', (error) => {
  if (error) {
    return console.log(error);
  }
});
