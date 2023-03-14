#!/usr/bin/node
/**
 *  a script that imports a dictionary of occurrences by user id and computes a
 * dictionary of user ids by occurrence
 */

const dict = require('./101-data').dict;
let array = [];
const dict2 = {};
const values = Object.values(dict);
const keys = Object.keys(dict);

for (let i = 0; i < keys.length; i++) {
  for (let j = 0; j < keys.length; j++) {
    if (dict[keys[i]] === values[j]) {
      array.push(keys[j]);
      dict2[values[i]] = array;
    }
  }
  array = [];
}
console.log(dict2);
