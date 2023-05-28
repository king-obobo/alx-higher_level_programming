#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const API = 'https://swapi-api.alx-tools.com/api/films/';

request(API + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const response = JSON.parse(body);
    console.log(response.title);
  }
});
