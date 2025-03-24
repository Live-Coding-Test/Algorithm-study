const fs = require("fs");
const inputData = fs
  .readFileSync("./input.txt", "utf8")
  // .readFileSync("/dev/stdin", "utf8")
  .toString()
  .trim();

function solution(inputData) {
  const num = inputData.split("");
  const soltResult = num.sort((a, b) => b - a).join("");

  return soltResult === inputData ? "0" : soltResult;
}

console.log(solution(inputData));
