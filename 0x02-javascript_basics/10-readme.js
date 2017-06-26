#!/usr/bin/node
'use strict';
let text = process.argv[2];
let fs = require('fs');

fs.readFile(text, function (err, input) {
  if (err) {
    console.log('err - try again');
  }
  console.log(input);
});
