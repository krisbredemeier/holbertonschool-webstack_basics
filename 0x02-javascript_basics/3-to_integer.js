#!/usr/bin/node
// Write a script that prints "My number: "
//if the first argument can be converted to an integer:
"use strict";
let arg = process.argv;
//create counter
let i = 0;

if (i === 2) {
   console.log('No argument');
 } else {
  //prints first argument
  console.log(arg[2]);
  }
