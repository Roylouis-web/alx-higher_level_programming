#!/usr/bin/node
/**
 * Updates this script by adding a new function incr
 * that increments the integer value.
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = () => this.value++;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
