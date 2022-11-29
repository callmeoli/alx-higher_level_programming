#!/usr/bin/node
const Square1 = require('./5-Square');
class Square extends Square1 {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let S = '';
    let symbol = c;
    if (c === undefined) {
      symbol = 'X';
    }
    while (i < this.size) {
      while (j < this.size) {
        S = S + symbol;
        j++;
      }
      console.log(S);
      S = '';
      j = 0;
      i++;
    }
  }
}
module.exports = Square;
