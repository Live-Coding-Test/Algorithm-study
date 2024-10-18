const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const fluid = input
    .slice(1)
    .flat()
    .sort((a, b) => a - b);

  let start = 0;
  let end = N - 1;
  let sum = Infinity;
  let twoFluid = [];

  while (start < end) {
    const tempSum = fluid[start] + fluid[end];

    if (Math.abs(tempSum) < Math.abs(sum)) {
      sum = tempSum;
      twoFluid = [fluid[start], fluid[end]];
    }

    if (tempSum < 0) {
      start += 1;
    } else {
      end -= 1;
    }
  }

  return twoFluid.join(' ');
}

console.log(solution(input));
