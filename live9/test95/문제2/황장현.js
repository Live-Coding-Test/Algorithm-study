function solution(n, wires) {
  const graph = Array.from({ length: n + 1 }, () => []);

  for (let [w1, w2] of wires) {
    graph[w1].push(w2);
    graph[w2].push(w1);
  }

  let min = Infinity;

  for (let [cutA, cutB] of wires) {
    const visited = Array(n + 1).fill(false);

    function DFS(node) {
      visited[node] = true;
      let count = 1;

      for (const next of graph[node]) {
        if (!visited[next] && !(next === cutB)) {
          count += DFS(next);
        }
      }

      return count;
    }

    const countA = DFS(cutA);
    const countB = n - countA;

    min = Math.min(min, Math.abs(countA - countB));
  }

  return min;
}

console.log(
  solution(9, [
    [1, 3],
    [2, 3],
    [3, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [7, 8],
    [7, 9],
  ])
);
