#!/usr/bin/node
const arg = process.argv[2];
let i = 0;
if (isNaN(arg) || arg === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
