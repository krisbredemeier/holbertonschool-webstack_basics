#!/usr/bin/node
// Write a script that prints "My number: "
//if the first argument can be converted to an integer:
"use strict";
let arg = process.argv;
//create counter
let i = 0;

function isNumber( arg ) {
    return !isNaN( arg );
}

if (isNumber = false) {
   console.log('not a number');
 } else {
  //prints first argument
  console.log('My number:', arg[2]);
  }
