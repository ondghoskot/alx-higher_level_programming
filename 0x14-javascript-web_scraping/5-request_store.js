#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(filePath, body, 'utf8', (error) => {
    if (error) {
      return console.log(error);
    }
  });
});
