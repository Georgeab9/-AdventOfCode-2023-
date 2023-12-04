const fs = require("fs");

const EXAMPLE_INPUT = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`;

const TEXT_INPUT = fs.readFileSync("../input.txt", "utf8").split("\n");
const TEXT_EXAMPLE = EXAMPLE_INPUT.split("\n");

GOAL =
  "The Elf would first like to know which games would have been possible if the bag \
        contained only 12 red cubes, 13 green cubes, and 14 blue cubes?";

const example =
  "Game 5: 10 blue, 7 green, 2 red; 2 blue, 4 red; 2 green, 9 blue, 8 red";

// const gameId = example.split(": ")[0].replace(/\D/g, "");
// const gameSets = example.substring(example.trim().indexOf(":") + 1).split(";");

// let arr = 0;
// for (let elem of gameSets) {
//   const temp = elem.split(",");
//   for (let t of temp) {
//     const [count, colour] = t.trim().split(" ");
//     if (
//       (colour === "red" && count >= 12) ||
//       (colour === "blue" && count >= 14) ||
//       (colour === "green" && count >= 13)
//     ) {

//     }
//   }
// }

function sumPossible(lines) {
  let result = 0;

  for (let game of lines) {
    const gameId = parseInt(game.split(":")[0].replace(/\D/g, ""));
    const sets = game.substring(game.indexOf(":") + 1).split(";");

    let isPossible = true;
    for (let set of sets) {
      let redCount = 0,
        greenCount = 0,
        blueCount = 0;
      const colors = set.trim().split(", ");
      for (let color of colors) {
        const [count, colour] = color.split(" ");
        if (colour === "red") redCount += parseInt(count);
        if (colour === "green") greenCount += parseInt(count);
        if (colour === "blue") blueCount += parseInt(count);
      }

      if (redCount > 12 || greenCount > 13 || blueCount > 14) {
        isPossible = false;
        break;
      }
    }

    if (isPossible) {
      result += gameId;
    }
  }
  return result;
}
