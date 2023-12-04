const fs = require("fs");

const EXAMPLE_INPUT = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`;

const TEXT_INPUT = fs.readFileSync("../input.txt", "utf8").split("\n");

const lines = EXAMPLE_INPUT.split("\n");

let total = 0;

for (let line of TEXT_INPUT) {
  const arr = [];
  for (let char of line) {
    if (char >= "0" && char <= "9") {
      arr.push(char);
    }
  }
  if (arr.length > 1) {
    total += Number(arr[0] + arr[arr.length - 1]);
  } else if (arr.length === 1) {
    total += Number(arr[0] + arr[0]);
  } else {
    total += Number(0);
  }
}

console.log(total);
