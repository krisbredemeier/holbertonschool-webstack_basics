#!/usr/bin/node
//Write a script that prints a message depending
//of the number of arguments passed
"use strict";
function argvCounter() {
  for (var i = 0; i < 10; i++) {
    console.log(i)
  }
  console.log('arguments', i)
}
argvCounter()

if no argument console.log('No argument')
if 1 argument console.log('Argument found')
if < 1 argument console.log('Arguments found')
