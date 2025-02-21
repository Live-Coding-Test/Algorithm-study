const fs = require('fs');

const input = fs
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const relation = input.slice(1);
  const graph = Array.from({ length: N + 1 }).map((_) =>
    Array.from({ length: 0 })
  );

  for (const [f1, f2] of relation) {
    graph[f1].push(f2);
    graph[f2].push(f1);
  }

  function dfs(start, target) {}

  for (let i = 1; i <= N; i++) {
    const temp = [];
    for (let j = 1; j <= N; j++) {
      if (graph[i].includes(j)) temp.push(1);
      else dfs(i, j);
    }
  }
}

console.log(solution(input));
