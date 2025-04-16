const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, D] = input[0];
  const Info = input.slice(1);
  const dp = Array(D + 1).fill(Infinity);
  dp[0] = 0;

  const graph = Array.from({ length: D + 1 }, () => []);
  for (const [start, end, 지름길] of Info) {
    if (end > D) continue;
    if (end - start <= 지름길) continue;
    graph[start].push([end, 지름길]);
  }

  for (let i = 0; i <= D; i++) {
    if (i > 0) dp[i] = Math.min(dp[i], dp[i - 1] + 1);

    for (const [end, 지름길] of graph[i]) {
      if (dp[end] > dp[i] + 지름길) {
        dp[end] = dp[i] + 지름길;
      }
    }
  }

  return dp[D];
}

console.log(solution(input));
