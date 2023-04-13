#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, process.argv.length);
  const arranged = args.sort((a, b) => b - a);
  console.log(arranged[1]);
}
