#!/usr/bin/node
/**
 * a script that prints x times “C is fun”
 */

const process = require('process');
const args = process.argv;

if (args.length === 3) {
  const num = parseInt(args[2]);
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
} else if (args.length === 2 || isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
}
