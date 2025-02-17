const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M, V] = input[0];
  const graph = Array.from(Array(N + 1), () => Array(N + 1).fill(0));

  for (let i = 1; i <= M; i++) {
    let [row, column] = input[i];
    graph[row][column] = 1;
    graph[column][row] = 1;
  }

  const visited = new Array(N + 1).fill(false);
  const dfs_answer = [];
  const bfs_answer = [];

  function dfs(V) {
    visited[V] = true;
    dfs_answer.push(V);
    for (let i = 1; i < graph.length; i++) {
      if (graph[V][i] === 1 && !visited[i]) {
        dfs(i);
      }
    }
  }

  function bfs(V) {
    const queue = [];
    visited[V] = true;
    bfs_answer.push(V);
    queue.push(V);

    while (queue.length !== 0) {
      let dequeue = queue.shift();
      for (let i = 1; i < graph.length; i++) {
        if (graph[dequeue][i] === 1 && !visited[i]) {
          visited[i] = true;
          queue.push(i);
          bfs_answer.push(i);
        }
      }
    }
  }

  dfs(V);
  visited.fill(false);
  bfs(V);

  console.log(dfs_answer.join(' '));
  console.log(bfs_answer.join(' '));
}

solution(input);
