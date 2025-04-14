const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const n = input[0][0];
  const m = input[0][1];
  const busInfo = input.slice(2);
  const map = Array.from({ length: n }, () => Array(n).fill(Infinity));

  for (let i = 0; i < n; i++) {
    map[i][i] = 0;
  }

  for (const [start, end, cost] of busInfo) {
    map[start - 1][end - 1] = Math.min(map[start - 1][end - 1], cost);
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (map[i][j] > map[i][k] + map[k][j]) {
          map[i][j] = map[i][k] + map[k][j];
        }
      }
    }
  }

  return map
    .map((row) => row.map((cost) => (cost === Infinity ? 0 : cost)).join(' '))
    .join('\n');
}

console.log(solution(input));
