const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const n = Number(input[0]);
  const graph = {};

  for (let i = 1; i <= n; i++) {
    const [from, , to] = input[i].split(' ');
    if (!graph[from]) graph[from] = [];
    graph[from].push(to);
  }

  const m = Number(input[n + 1]);
  const queries = input.slice(n + 2);

  const results = [];

  function dfs(current, target, visited) {
    if (current === target) return true;
    if (!graph[current]) return false;

    for (const next of graph[current]) {
      if (!visited.has(next)) {
        visited.add(next);
        if (dfs(next, target, visited)) return true;
      }
    }
    return false;
  }

  for (const q of queries) {
    const [from, , to] = q.split(' ');
    const visited = new Set();
    visited.add(from);
    results.push(dfs(from, to, visited) ? 'T' : 'F');
  }

  return results.join('\n');
}

console.log(solution(input));
