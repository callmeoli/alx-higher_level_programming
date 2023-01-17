#!/usr/bin/node
/* a script that reads and prints the content of a file */

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log('Error: ', error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
