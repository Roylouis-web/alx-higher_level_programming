#!/usr/bin/node
/**
 * a class Square that defines a square and inherits
 *  from Rectangle of 4-rectangle.js
 */

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = '';
    if (c) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          if (j === this.width - 1 && i !== this.width - 1) {
            str += c + '\n';
          } else {
            str += c;
          }
        }
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          if (j === this.width - 1 && i !== this.width - 1) {
            str += 'X\n';
          } else {
            str += 'X';
          }
        }
      }
    }

    console.log(str);
  }
}

module.exports = Square;
