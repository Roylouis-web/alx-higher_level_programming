#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 3) {
  const number = parseInt(args[2]);
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + number);
  }
} else if (args.length === 2) {
  console.log('Not a number');
}
