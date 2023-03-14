#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 3) {
  const num = parseInt(args[2]);
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else if (typeof (num) !== 'number') {
    console.log('Missing number of occurrences');
  }
} else if (args.length === 2) {
  console.log('Missing number of occurrences');
}
