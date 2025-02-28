const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const T = input[0];
  let index = 1;
  const result = [];
  for (let i = 0; i < T; i++) {
    const N = input[index];
    const X = input[index + 1].sort((a, b) => a - b);
    index += 2;

    const XSet = new Set(X);

    let count = 0;
    for (let p1 = 0; p1 < N - 2; p1++) {
      for (let p2 = p1 + 2; p2 < N; p2++) {
        const mid = (X[p1] + X[p2]) / 2;
        if (Number.isInteger(mid) && XSet.has(mid)) {
          count++;
        }
      }
    }

    result.push(count);
  }
  return result.join('\n');
}

console.log(solution(input));
