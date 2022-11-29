#!/usr/bin/node
const x = process.argv[2];
const y = process.argv[3];

const parsed = parseInt(x, 10);
const parsed2 = parseInt(y, 10);

function add (a, b) {
  const c = a + b;
  return c;
}

if (isNaN(parsed) || isNaN(parsed2)) {
  console.log('NaN');
} else {
  console.log(add(parsed, parsed2));
}
