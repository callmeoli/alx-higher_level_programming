#!/usr/bin/node
const x = process.argv[2];
const parsed = parseInt(x, 10);
if (isNaN(parsed)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parsed) {
    console.log('C is fun');
    i++;
  }
}
