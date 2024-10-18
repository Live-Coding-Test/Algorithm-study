const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const n = input[0][0];
  const numArray = input[1].sort((a, b) => a - b);
  const x = input[2][0];

  let count = 0;
  let start = 0;
  let end = n - 1;

  while (start < end) {
    const tempSum = numArray[start] + numArray[end];

    if (tempSum === x) {
      count++;
      start += 1;
      end -= 1;
    } else if (tempSum < x) {
      start += 1;
    } else {
      end -= 1;
    }
  }

  return count;
}

console.log(solution(input));
