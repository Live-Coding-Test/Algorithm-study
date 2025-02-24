const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [K, N] = input[0];
  const lanList = input.slice(1).flat();
  if (K >= N) return Math.max(...lanList);
}

console.log(solution(input));
