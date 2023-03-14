#!/usr/bin/node
/**
 * a script that prints a square
 */

const process = require('process');
const args = process.argv;

if (args.length === 3) {
  const num = parseInt(args[2]);
  let str = '';
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        if (j === num - 1 && i != num - 1) {
          str += 'X\n';
        } else {
          str += 'X';
        }
      }
    }
    console.log(str);
  } else if (typeof (num) !== 'number') {
    console.log('Missing size');
  }
} else if (args.length === 2) {
  console.log('Missing size');
}
