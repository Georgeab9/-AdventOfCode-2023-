const fs = require("fs");

const EXAMPLE_INPUT = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`;

const EXPECTED_OUTPUT = 2286;

const TEXT_INPUT = fs.readFileSync("../input.txt", "utf8").split("\n");
const TEXT_EXAMPLE = EXAMPLE_INPUT.split("\n");

function getMaximumSum(games) {
  let finalResult = 0;

  games.forEach((game) => {
    let redMax = 0,
      greenMax = 0,
      blueMax = 0;
    const sets = game.substring(game.indexOf(":") + 1).split(";");

    sets.forEach((set) => {
      const colors = set.trim().split(", ");
      colors.forEach((color) => {
        const [count, colour] = color.split(" ");
        const numCount = parseInt(count);
        if (colour === "red" && numCount > redMax) redMax = numCount;
        if (colour === "green" && numCount > greenMax) greenMax = numCount;
        if (colour === "blue" && numCount > blueMax) blueMax = numCount;
      });
    });

    finalResult += redMax * greenMax * blueMax;
  });

  return finalResult;
}

console.log(getMaximumSum(TEXT_INPUT));
