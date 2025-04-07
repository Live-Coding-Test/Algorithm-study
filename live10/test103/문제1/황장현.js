const fs = require('fs');
const input = fs
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function solution(input) {
  let N = input;
  let count = 0;

  while (N >= 0) {
    if (N % 5 === 0) {
      count += N / 5;
      return count;
    }
    N -= 3;
    count++;
  }

  return -1;
}

console.log(solution(input));
