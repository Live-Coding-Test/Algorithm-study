const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const N = Number(input[0]);
  const relations = input.slice(1).map((line) => line.split(''));

  let max = 0;

  for (let i = 0; i < N; i++) {
    const set = new Set();

    for (let j = 0; j < N; j++) {
      if (i === j) continue;

      if (relations[i][j] === 'Y') {
        set.add(j);
      } else {
        for (let k = 0; k < N; k++) {
          if (relations[i][k] === 'Y' && relations[k][j] === 'Y') {
            set.add(j);
            break;
          }
        }
      }
    }

    max = Math.max(max, set.size);
  }
  return max;
}

console.log(solution(input));
