#!/usr/bin/node
// Write a script that reads and prints the content of a file.
'use strict';
let text = process.argv[2];
let fs = require('fs');

fs.readFile(text, function (err, data) {
  //if (err) {
  //  console.log('err - try again');
  //}
  console.log(data);
});
