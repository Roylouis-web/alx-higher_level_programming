#!/usr/bin/node
/**
 * a script that prints the addition of 2 integers
 */

function add (a, b) {
  console.log(a + b);
}

const process = require('process');
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
add(a, b);
