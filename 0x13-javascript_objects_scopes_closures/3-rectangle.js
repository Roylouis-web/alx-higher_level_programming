#!/usr/bin/node
/**
 *  a class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (j === this.width - 1 && i !== this.height - 1) {
          str += 'X\n';
        } else {
          str += 'X';
        }
      }
    }

    console.log(str);
  }
}

module.exports = Rectangle;
