#!/usr/bin/node

const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const object = JSON.parse(body);
    console.log(object.title);
  }
});
