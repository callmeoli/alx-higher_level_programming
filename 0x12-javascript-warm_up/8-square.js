#!/usr/bin/node
const x = process.argv[2];
const parsed = parseInt(x, 10);
if (isNaN(parsed)) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  let S = '';
  while (i < parsed) {
    while (j < parsed) {
      S = S + 'X';
      j++;
    }
    console.log(S);
    S = '';
    j = 0;
    i++;
  }
}
