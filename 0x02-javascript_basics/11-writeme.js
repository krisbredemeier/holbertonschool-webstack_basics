#!/usr/bin/node
// Write a script that writes a string to a file
'use strict';
let text = process.argv[2];
let fs = require('fs');

fs.writeFile(text, function (err) {
  if (err) throw err;
  console.log('Saved!');
});
