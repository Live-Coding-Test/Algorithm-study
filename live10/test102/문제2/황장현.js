const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const an = input[1];

  let current = an[0];
  let maxProfit = 0;

  for (const a of an) {
    maxProfit = Math.max(maxProfit, a - current);

    current = Math.min(current, a);
  }

  return maxProfit;
}

console.log(solution(input));
