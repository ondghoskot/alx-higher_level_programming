#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, code) => {
  if (error) {
    return console.log(error);
  } else {
    console.log('code:', code.statusCode);
  }
});
