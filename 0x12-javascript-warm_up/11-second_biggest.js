#!/usr/bin/node
const x = process.argv;
const b = x.length;
let max = parseInt(process.argv[2], 10);
let max2 = parseInt(process.argv[2], 10);

if (b <= 3) {
  console.log(0);
} else {
  for (let i = 3; i <= b; i++) {
    if (process.argv[i] > max) {
      max2 = max;
      max = process.argv[i];
    } else if (process.argv[i] > max2) {
      max2 = process.argv[i];
    }
  }
  console.log(max2);
}
