const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const 지방예산요청 = input[1].sort((a, b) => a - b);
  const M = input[2][0];

  let high = 지방예산요청[N - 1];
  let low = 0;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const sum = 지방예산요청.reduce((acc, v) => acc + (v <= mid ? v : mid), 0);
    if (sum > M) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return high;
}

console.log(solution(input));
