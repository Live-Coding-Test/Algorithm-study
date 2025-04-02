const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const cost = input.slice(1);
  const dp = Array.from({ length: N + 1 }, () => Array(3).fill(0));

  dp[1][0] = cost[0][0];
  dp[1][1] = cost[0][1];
  dp[1][2] = cost[0][2];

  for (let i = 2; i <= N; i++) {
    dp[i][0] = cost[i - 1][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
    dp[i][1] = cost[i - 1][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
    dp[i][2] = cost[i - 1][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
  }

  return Math.min(dp[N][0], dp[N][1], dp[N][2]);
}

console.log(solution(input));
