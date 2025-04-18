const input = require("fs")
  .readFileSync(
    process.platform === "linux"
      ? "/dev/stdin"
      : require("path").join(__dirname, "input.txt"),
    "utf8"
  )
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const [N, M] = input[0].split(" ").map(Number);
  const dots = input[1].split(" ").map(Number);
  const lines = input.slice(2).map((line) => line.split(" ").map(Number));
  const result = [];

  for (let [a, b] of lines) {
    let count = 0;
    for (let x of dots) {
      if (x >= a && x <= b) count++;
    }
    result.push(count);
  }

  return result.join("\n");
}

console.log(solution(input));
