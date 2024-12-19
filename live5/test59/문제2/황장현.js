const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const arr = input.slice(1, N + 1);
  const K = input[N + 1][0];
  const result = [];

  const prefixSum = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));

  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= M; j++) {
      prefixSum[i][j] =
        arr[i - 1][j - 1] +
        prefixSum[i - 1][j] +
        prefixSum[i][j - 1] -
        prefixSum[i - 1][j - 1];
    }
  }

  for (let e = N + 2; e < N + 2 + K; e++) {
    const [i, j, x, y] = input[e];
    const currentSum =
      prefixSum[x][y] -
      prefixSum[i - 1][y] -
      prefixSum[x][j - 1] +
      prefixSum[i - 1][j - 1];
    result.push(currentSum);
  }

  return result.join('\n');
}

console.log(solution(input));
