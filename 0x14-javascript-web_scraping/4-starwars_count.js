#!/usr/bin/node
/* a script that reads and prints the content of a file */

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const resutls = JSON.parse(body).results;
    console.log(resutls);
    const valueToCount = 'https://swapi-api.alx-tools.com/api/people/18/';
    const count = Object.values(resutls).reduce((n, val) => n + (val === valueToCount), 0);
    console.log(count);
  }
});
