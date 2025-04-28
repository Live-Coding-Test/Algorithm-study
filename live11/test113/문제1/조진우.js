const input = require("fs")
  .readFileSync(
    process.platform === "linux"
      ? "/dev/stdin"
      : require("path").join(__dirname, "input.txt"),
    "utf8"
  )
  .trim()
  .split("\n");

function solution(input) {
  let index = 0;
  const T = Number(input[index++]);
  const output = [];

  for (let t = 0; t < T; t++) {
    const N = Number(input[index++]);
    const numbers = [];

    for (let i = 0; i < N; i++) {
      numbers.push(input[index++]);
    }

    numbers.sort();

    output.push(consistent ? "YES" : "NO");
  }

  return output.join("\n");
}

console.log(solution(input));
