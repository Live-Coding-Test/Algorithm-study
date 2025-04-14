function solution(m, n, puddles) {
  const dp = Array.from({ length: n }, () => Array(m).fill(0));

  for (const puddle of puddles) {
    const [col, row] = puddle;

    dp[row - 1][col - 1] = -1;
  }

  for (let i = 0; i < m; i++) {
    if (dp[0][i] === -1) {
      break;
    }

    dp[0][i] = 1;
  }

  for (let i = 0; i < n; i++) {
    if (dp[i][0] === -1) {
      break;
    }

    dp[i][0] = 1;
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
      if (dp[i][j] === -1) {
        continue;
      }

      if (dp[i - 1][j] === -1 || dp[i][j - 1] === -1) {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      } else {
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007;
      }
    }
  }

  return dp[n - 1][m - 1];
}
console.log(solution(4, 3, [[2, 2]]));
