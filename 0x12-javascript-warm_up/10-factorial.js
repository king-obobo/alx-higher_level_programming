#!/usr/bin/node
let num = process.argv[2];
let i = num;
if (isNaN(num)) {
  console.log(1);
} else {
  while (i > 1) {
    num = num * (i - 1);
    i--;
  } console.log(num);
}
