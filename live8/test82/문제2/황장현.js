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
  const graph = Array.from({ length: N + 1 }, () => []);

  for (const [f1, f2] of relation) {
    graph[f1].push(f2);
    graph[f2].push(f1);
  }

  function bfs(start, target) {
    const queue = [[start, 0]];
    const visited = Array(N + 1).fill(false);
    visited[start] = true;

    while (queue.length > 0) {
      const [current, depth] = queue.shift();

      if (current === target) return depth;

      for (let nearNode of graph[current]) {
        if (!visited[nearNode]) {
          visited[nearNode] = true;
          queue.push([nearNode, depth + 1]);
        }
      }
    }
    return Infinity;
  }

  let minKevinBacon = Infinity;
  let minUser = -1;

  for (let i = 1; i <= N; i++) {
    let kevinBacon = 0;
    for (let j = 1; j <= N; j++) {
      if (i !== j) {
        kevinBacon += bfs(i, j);
      }
    }

    if (kevinBacon < minKevinBacon) {
      minKevinBacon = kevinBacon;
      minUser = i;
    } else if (kevinBacon === minKevinBacon) {
      minUser = Math.min(minUser, i);
    }
  }

  console.log(minUser);
}

solution(input);
