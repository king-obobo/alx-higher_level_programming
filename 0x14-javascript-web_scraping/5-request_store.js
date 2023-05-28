#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const filePath = process.argv[3];

request(URL, function (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
