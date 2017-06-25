#!/usr/bin/node
//Write a script that prints the first argument passed to it:
"use strict";
let argv = process.argv;

if (argv < 3) {
   console.log('No argument');
  }
if (argv > 3) {
  console.log(argv);
  }
