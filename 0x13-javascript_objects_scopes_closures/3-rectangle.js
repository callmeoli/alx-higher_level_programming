#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let S = '';
    while (i < this.height) {
      while (j < this.width) {
        S = S + 'X';
        j++;
      }
      console.log(S);
      S = '';
      j = 0;
      i++;
    }
  }
}
module.exports = Rectangle;
