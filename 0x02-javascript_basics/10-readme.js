#!/usr/bin/node
'use strict';
let text = process.argv[2];
let fs = require('fs');

fs.toFile(text, function (err, input){
  if (err) throw err;
  console.log(input);
});
