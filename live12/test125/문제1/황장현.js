const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

const N = input[0][0];
const home = input.slice(1);

let answer = Infinity;

// 0: R, 1: G, 2: B
for (let firstColor = 0; firstColor < 3; firstColor++) {
  const dp = Array.from({ length: N }, () => Array(3).fill(Infinity));

  dp[0][firstColor] = home[0][firstColor];

  for (let i = 1; i < N; i++) {
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + home[i][0]; // R
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + home[i][1]; // G
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + home[i][2]; // B
  }

  for (let lastColor = 0; lastColor < 3; lastColor++) {
    if (lastColor !== firstColor) {
      answer = Math.min(answer, dp[N - 1][lastColor]);
    }
  }
}

console.log(answer);
