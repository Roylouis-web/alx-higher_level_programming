#!/usr/bin/node
/**
 * a script that computes and prints a factorial
 */

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
console.log(factorial(num));
