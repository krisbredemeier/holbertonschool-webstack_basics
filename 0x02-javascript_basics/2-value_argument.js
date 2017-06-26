#!/usr/bin/node
// Write a script that prints the first argument passed to it:
'use strict';
let arg = process.argv;
// create counter
let i = 0;

while (arg[i]) {
  i++;
}
if (i === 2) {
  console.log('No argument');
} else {
  // prints first argument
  console.log(arg[2]);
}
