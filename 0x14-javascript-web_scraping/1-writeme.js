#!/usr/bin/node
/* a script that reads and prints the content of a file */

const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];
fs.writeFile(filename, content, 'utf8', (err) => { if (err) throw err; });
