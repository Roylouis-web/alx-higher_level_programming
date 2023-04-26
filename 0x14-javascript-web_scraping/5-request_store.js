#!/usr/bin/node

const process = require('process');
const request = require('request');
const { createWriteStream } = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url)
  .on('error', (e) => {
    console.log(e);
  })
  .pipe(createWriteStream(file));
