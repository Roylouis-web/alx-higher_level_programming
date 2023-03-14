#!/usr/bin/node
/**
 * a script that imports an array and computes a new array.
 */

const list = require('./100-data').list;
const arr = list.map(elem => elem * list.indexOf(elem));
console.log(list);
console.log(arr);
