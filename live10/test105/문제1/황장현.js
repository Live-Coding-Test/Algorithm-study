const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M, K, X] = input[0];
  const graph = Array.from({ length: N + 1 }, () => []);
  const visited = Array.from({ length: N + 1 }, () => false);
  const info = input.slice(1);

  for (let i = 0; i < M; i++) {
    const [a, b] = info[i];
    graph[a].push(b);
  }
  const queue = [];
  const result = [];
  queue.push([X, 0]);
  visited[X] = true;
  while (queue.length) {
    const [node, cnt] = queue.shift();
    if (cnt === K) {
      result.push(node);
      continue;
    }
    for (const next of graph[node]) {
      if (!visited[next]) {
        visited[next] = true;
        queue.push([next, cnt + 1]);
      }
    }
  }
  result.sort((a, b) => a - b);
  if (result.length === 0) {
    return -1;
  }
  return result.join('\n');
}

console.log(solution(input));
