#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printChars(chars, 0);
  }
});

const printChars = function (chars, idx) {
  request(chars[idx], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printChars(chars, idx + 1);
      }
    }
  });
};
