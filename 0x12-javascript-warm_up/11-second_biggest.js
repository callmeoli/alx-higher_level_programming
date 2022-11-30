#!/usr/bin/node
const x = process.argv;
const b = x.length;
let max = parseInt(process.argv[2], 10);
let max2 = parseInt(process.argv[2], 10);

if (b <= 3) {
  console.log(0);
} else {
  for (let i = 3; i <= b; i++) {
    if (parseInt(process.argv[i], 10) > max) {
      max2 = max;
      max = parseInt(process.argv[i], 10);
    } else if (parseInt(process.argv[i], 10) > max2) {
      max2 = parseInt(process.argv[i], 10);
    }
  }
  console.log(max2);
}
