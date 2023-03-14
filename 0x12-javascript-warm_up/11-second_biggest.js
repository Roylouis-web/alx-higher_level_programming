#!/usr/bin/node
/**
 *  a script that searches the second biggest
 *  integer in the list of arguments.
 */

/**
 *
 * @param {array parameter} array
 * @returns an integer
 */

function max (array) {
  let max = array[0];
  array.forEach(element => {
    if ((element) > max) {
      max = element;
    }
  });
  return max;
}

/**
 *
 * @param {array parameter} array
 */

function secondBiggest (array) {
  if (array.length === 2 || array.length === 3) {
    console.log(0);
  } else {
    const arr = [];
    for (let i = 2; i < array.length; i++) {
      arr.push(parseInt(array[i]));
    }
    const num = max(arr);
    const index = arr.indexOf(num);
    arr.splice(index, 1);
    const num2 = max(arr);
    console.log(num2);
  }
}

const process = require('process');
const args = process.argv;
secondBiggest(args);
