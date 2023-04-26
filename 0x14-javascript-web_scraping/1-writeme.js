#!/usr/bin/node

const { writeFile } = require('fs');
const process = require('process');
const file = process.argv[2];
const text = process.argv[3];

writeFile(file, text, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.log(err);
  }
});
