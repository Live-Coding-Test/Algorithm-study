const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const An = input[1];
  const M = input[2][0];
  const result = [];

  const prefixSum = new Array(N + 1).fill(0);

  for (let i = 1; i <= N; i++) {
    prefixSum[i] = prefixSum[i - 1] + An[i - 1];
  }

  for (let k = 3; k < 3 + M; k++) {
    const [i, j] = input[k];
    const totalSum = prefixSum[j] - prefixSum[i - 1];
    result.push(totalSum);
  }

  return result.join('\n');
}

console.log(solution(input));
