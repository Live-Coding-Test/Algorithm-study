const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input.map(Number).splice(1);

arr.sort((a, b) => a - b);

let min = Number.MAX_SAFE_INTEGER;

for (let i = 0; i < N; i++) {
  const set = new Set([arr[i] + 1, arr[i] + 2, arr[i] + 3, arr[i] + 4]);
  let cnt = 0;
  for (let j = 0; j < N; j++) {
    if (set.has(arr[j])) cnt++;
  }
  min = Math.min(cnt, min);
}

console.log(min);
