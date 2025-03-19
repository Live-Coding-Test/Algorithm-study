function solution(k, dungeons) {
  let maxDepth = 0;

  function DFS(현재피로도, currentDepth, visited) {
    maxDepth = Math.max(maxDepth, currentDepth);

    for (let i = 0; i < dungeons.length; i++) {
      if (visited[i]) continue;

      const [최소필요피로도, 소모피로도] = dungeons[i];

      if (현재피로도 >= 최소필요피로도) {
        visited[i] = true;
        DFS(현재피로도 - 소모피로도, currentDepth + 1, visited);
        visited[i] = false;
      }
    }
  }

  const visited = Array(dungeons.length).fill(false);
  DFS(k, 0, visited);

  return maxDepth;
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
);
