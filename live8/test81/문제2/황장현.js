const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const M = input[1][0];
  const computerList = input.slice(2);

  const graph = Array.from({ length: N + 1 }, () => []);
  const visited = Array.from({ length: N + 1 }).fill(false);

  for (let [c1, c2] of computerList) {
    graph[c1].push(c2);
    graph[c2].push(c1);
  }
  let count = 0;

  function dfs(node) {
    count++;
    visited[node] = true;
    const list = graph[node];
    for (let i = 0; i < list.length; i++) {
      if (!visited[list[i]]) dfs(list[i]);
    }
  }
  dfs(1);
  return count - 1;
}

console.log(solution(input));
