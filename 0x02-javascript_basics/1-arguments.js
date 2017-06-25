#!/usr/bin/node
//Write a script that prints a message depending
//of the number of arguments passed
"use strict";
let argvLen = process.argv.length;

if (argvLen < 3) {
   console.log('No argument');
}

if (argvLen === 3) {
  console.log('Argument found');
}

if (argvLen > 3) {
  console.log('Arguments found');
}
