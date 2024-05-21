#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
request(`${endpoint}${movieId}`, (error, response, body) => {
  if (error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
