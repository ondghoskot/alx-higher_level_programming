#!/usr/bin/node
const request = require('request');
const starWarsApi = process.argv[2];
const characterId = '18';
request(`${endpoint}${movieId}`, (error, response, body) => {
  if (error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
