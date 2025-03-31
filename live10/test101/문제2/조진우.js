const fs = require("fs");
const path = require("path");

const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : path.join(__dirname, "input.txt");

const input = fs
  .readFileSync(filePath, "utf8")
  .toString()
  .trim()
  .split("\n")
  .map((value) => value.split(" ").map(Number));

function solution(input) {
  const N = input[0][0];
  const costs = input.slice(1);
  const result = [];

  function dfs(index, color) {
    if (index === 0) return costs[0][color];

    let minCost = Infinity;

    for (let i = 0; i < 3; i++) {
      if (i !== color) {
        const cost = dfs(index - 1, i) + costs[index][color];
        if (cost < minCost) minCost = cost;
      }
    }

    return minCost;
  }

  const lastHouse = N - 1;

  const minTotal = Math.min(
    dfs(lastHouse, 0),
    dfs(lastHouse, 1),
    dfs(lastHouse, 2)
  );

  result.push(minTotal);

  return result;
}

console.log(solution(input).join("\n"));
