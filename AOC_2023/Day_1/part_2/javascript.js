const fs = require("fs");

const EXAMPLE_INPUT = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
rxnhdflsqdqglxdmfxlxponeseven4one`;

const TEXT_INPUT = fs.readFileSync("../input.txt", "utf8").split("\n");
const TEXT_EXAMPLE = EXAMPLE_INPUT.split("\n");

const EXPECTED_OUTPUT = 55429;

const num_map = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};

const number_map = new Map([
  ["one", 1],
  ["two", 2],
  ["three", 3],
  ["four", 4],
  ["five", 5],
  ["six", 6],
  ["seven", 7],
  ["eight", 8],
  ["nine", 9],
]);

const example = "eightwothree";

// for (const [key, value] of Object.entries(num_map)) {
//   console.log(`Key: ${key}, Value: ${value}`);
// }

// let arr = [];
// for (const [key, value] of number_map.entries()) {
//   const search = key;
//   let letterIndex = example.indexOf(search);

//   while (letterIndex !== -1) {
//     arr.push({ [value]: letterIndex });
//     letterIndex = example.indexOf(search, letterIndex + 1);
//   }
// }

// for (let char of example) {
//   if (char >= "0" && char <= "9") {
//     arr.push({ [char]: example.indexOf(char) });
//   }
// }

// const sortedPairs = arr.flatMap(Object.entries).sort((a, b) => a[1] - b[1]);
// const newArray = sortedPairs.map((pair) => parseInt(pair[0]));

// let total = 0;
// if (newArray.length > 1) {
//   total += Number(String(newArray[0]) + String(newArray[newArray.length - 1]));
// } else if (newArray.length === 1) {
//   total += Number(String(newArray[0]) + String(newArray[0]));
// }

function findSum(string) {
  let arr = [];
  for (const [key, value] of number_map.entries()) {
    const search = key;
    let letterIndex = string.indexOf(search);

    while (letterIndex !== -1) {
      arr.push({ [value]: letterIndex });
      letterIndex = string.indexOf(search, letterIndex + 1);
    }
  }

  for (let char of string) {
    if (char >= "0" && char <= "9") {
      arr.push({ [char]: string.indexOf(char) });
    }
  }

  const sortedPairs = arr.flatMap(Object.entries).sort((a, b) => a[1] - b[1]);
  const newArray = sortedPairs.map((pair) => parseInt(pair[0]));

  let total = 0;
  if (newArray.length > 1) {
    total += Number(
      String(newArray[0]) + String(newArray[newArray.length - 1])
    );
  } else if (newArray.length === 1) {
    total += Number(String(newArray[0]) + String(newArray[0]));
  }

  return total;
}

const totals = TEXT_INPUT.map(findSum);
const totalSum = totals.reduce((tot, val) => tot + val, 0);
console.log(totalSum);
