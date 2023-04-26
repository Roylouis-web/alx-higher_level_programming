#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];
let count = 0;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const object = JSON.parse(body);
    for (const character of object.results) {
      for (const char of character.characters) {
        const regex = /https:\/\/swapi-api.alx-tools.com\/api\/people\/18\//;
        if (regex.test(char)) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
