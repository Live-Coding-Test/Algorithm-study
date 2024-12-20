const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const [N, M] = input[0].split(' ').map(Number);

  let prefixSum = Array.from({ length: N }, () => Array(M).fill(0));

  let arr = [];
  for (let i = 1; i <= N; i++) {
    arr.push([...input[i].split(' ').map(Number)]);
  }

  // Prefix sum 배열을 채우기
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (i === 0 && j === 0) {
        prefixSum[i][j] = arr[i][j];
      } else if (i === 0) {
        prefixSum[i][j] = prefixSum[i][j - 1] + arr[i][j];
      } else if (j === 0) {
        prefixSum[i][j] = prefixSum[i - 1][j] + arr[i][j];
      } else {
        prefixSum[i][j] =
          arr[i][j] +
          prefixSum[i - 1][j] +
          prefixSum[i][j - 1] -
          prefixSum[i - 1][j - 1];
      }
    }
  }

  const K = Number(input[N + 1]);
  let results = [];

  for (let k = 0; k < K; k++) {
    const [i, j, x, y] = input[N + 2 + k].split(' ').map(Number);
    let sum = prefixSum[x - 1][y - 1];

    if (i > 1) sum -= prefixSum[i - 2][y - 1];
    if (j > 1) sum -= prefixSum[x - 1][j - 2];
    if (i > 1 && j > 1) sum += prefixSum[i - 2][j - 2];

    results.push(sum);
  }

  return results.join('\n');
}

console.log(solution(input));
