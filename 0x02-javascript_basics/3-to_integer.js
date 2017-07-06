#!/usr/bin/node
// Write a script that prints "My number: "
// if the first argument can be converted to an integer:
'use strict';
let arg = process.argv;

if (isNaN(arg[2]) === true) {
  console.log('Not a number');
}
if (isNaN(arg[2]) === false) {
  // prints first argument
  console.log('My number:', arg[2]);
}
