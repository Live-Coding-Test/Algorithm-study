const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const arrA = input[1];

  let max = 0;
  function diffMax(arr, visited) {
    if (arr.length == N) {
      let sum = 0;

      for (let i = 0; i < N - 1; i++) {
        sum += Math.abs(arr[i] - arr[i + 1]);
      }
      if (sum > max) max = sum;
      return;
    } else {
      for (let i = 0; i < N; i++) {
        if (!(visited & (1 << i))) {
          arr.push(arrA[i]);
          diffMax(arr, visited | (1 << i));
          arr.pop();
        }
      }
    }
  }

  diffMax([], 0);

  return max;
}

console.log(solution(input));
