#!/usr/bin/node
const size = process.argv[2];
let i = 0;
if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
