const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

const N = input[0][0];
const lines = input.slice(1).sort((a, b) => a[0] - b[0]);

let totalLength = 0;
let currentStart = lines[0][0];
let currentEnd = lines[0][1];

for (let i = 1; i < N; i++) {
  const [start, end] = lines[i];

  if (start <= currentEnd) {
    currentEnd = Math.max(currentEnd, end);
  } else {
    totalLength += currentEnd - currentStart;
    currentStart = start;
    currentEnd = end;
  }
}

totalLength += currentEnd - currentStart;

console.log(totalLength);
