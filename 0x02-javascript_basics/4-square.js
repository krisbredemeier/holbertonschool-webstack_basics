#!/usr/bin/node
// Write a script that prints a square
'use strict';
let arg = process.argv;
let i, j, row;

if (isNaN(arg[2]) === true) {
  console.log('Missing size');
} else {
   // loop through argument number to print square
  for (i = 0; i < arg[2]; i++) {
    row = '';
    for (j = 0; j < arg[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
  // console.log('My number:', arg[2]);
}
