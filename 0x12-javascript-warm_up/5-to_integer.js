#!/usr/bin/node
const x = process.argv[2];
const parsed = parseInt(x, 10);
if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log(parsed);
}
