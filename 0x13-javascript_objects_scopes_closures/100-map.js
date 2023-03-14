#!/usr/bin/node
/**
 * a script that imports an array and computes a new array.
 */

const list = require('./100-data').list;
const arr = [];

for (let i = 0; i < list.length; i++) {
  arr.push(list[i] * i);
}
console.log(list);
console.log(arr);
