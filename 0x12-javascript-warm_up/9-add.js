#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const process = require('process');
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
add(a, b);
