const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

const [N, K] = input;

const dp = Array.from({ length: K + 1 }, () => Array(N + 1).fill(0));

for (let i = 0; i <= K; i++) {
  dp[i][0] = 1;
}

for (let i = 1; i <= K; i++) {
  for (let j = 1; j <= N; j++) {
    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000;
  }
}

console.log(dp[K][N]);
