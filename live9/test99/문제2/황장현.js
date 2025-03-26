const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const number = input[1].sort((a, b) => a - b);

  const visited = Array(N).fill(false);
  const path = [];
  const result = [];

  function dfs(depth) {
    if (depth === M) {
      result.push(path.join(' '));
      return;
    }

    for (let i = 0; i < N; i++) {
      if (!visited[i]) {
        visited[i] = true;
        path.push(number[i]);
        dfs(depth + 1);
        path.pop();
        visited[i] = false;
      }
    }
  }

  dfs(0);

  return result.join('\n');
}

console.log(solution(input));
