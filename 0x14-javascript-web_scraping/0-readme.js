#!/usr/bin/node

const { readFile } = require('fs');
const process = require('process');
const file = process.argv[2];

readFile(file, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
