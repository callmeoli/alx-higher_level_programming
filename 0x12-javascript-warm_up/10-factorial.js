#!/usr/bin/node
const x = process.argv[2];
const parsed = parseInt(x, 10);

function factorial (b) {
  if (b === 0) {
    return 1;
  }
  return b * factorial(b - 1);
}

if (isNaN(parsed)) {
  console.log(1);
} else {
  console.log(factorial(parsed));
}
