const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const T = input[0][0];
  const dp = Array(12).fill(0);
  const result = [];
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;

  function 재귀(n) {
    if (dp[n] !== 0) return dp[n];

    dp[n] = 재귀(n - 1) + 재귀(n - 2) + 재귀(n - 3);
    return dp[n];
  }

  for (let i = 1; i <= T; i++) {
    const currentIndex = input[i][0];
    result.push(재귀(currentIndex));
  }
  return result.join('\n');
}

console.log(solution(input));
