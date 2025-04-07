const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const T = input[0][0];
  const nums = input.slice(1);
  const dp = Array(101).fill(0);

  dp[1] = 1;
  dp[2] = 1;
  dp[3] = 1;
  dp[4] = 2;
  dp[5] = 2;

  for (let i = 6; i <= 100; i++) {
    dp[i] = dp[i - 1] + dp[i - 5];
  }

  return nums.map((n) => dp[n]).join('\n');
}

console.log(solution(input));
