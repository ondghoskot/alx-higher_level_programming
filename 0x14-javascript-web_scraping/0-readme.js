#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    return console.log(error);
  } else {
    console.log(data);
  }
});
