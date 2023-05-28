#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + id, function (error, res, body) {
  if (!error) {
    const data = JSON.parse(body);
    const chars = data.characters;
    for (const i of chars) {
      request.get(i, function (err, res, body1) {
        if (!err) {
          const data1 = JSON.parse(body1);
          console.log(data1.name);
        }
      });
    }
  }
});
