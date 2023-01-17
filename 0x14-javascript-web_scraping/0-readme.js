#!/usr/bin/node
/* a script that reads and prints the content of a file */

const fs = require('fs');
const filename = process.argv[2];
try {
  const data = fs.readFileSync(filename, 'utf8');
  console.log(data);
} catch (err) {
  console.log('Something went wrong: ' + err);
}
