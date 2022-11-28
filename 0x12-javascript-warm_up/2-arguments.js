#!/usr/bin/node
const process = require('process');

const argv = process.argv;
// print process.argv
let i = 0;
argv.forEach((val, index) => {
  i = index;
});

if (i === 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
