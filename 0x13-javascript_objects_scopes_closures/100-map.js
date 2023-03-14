#!/usr/bin/node
/**
 * a script that imports an array and computes a new array.
 */

const list = require('./100-data').list;
let i = 0;
const arr = list.map((elem) => {
  return elem * i++;
});
console.log(list);
console.log(arr);
