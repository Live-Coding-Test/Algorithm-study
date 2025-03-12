function DFS(v, visited, com_size, computers) {
  visited[v] = true;

  for (let w = 0; w < com_size; w++) {
    if (computers[v][w] !== 0 && !visited[w]) {
      DFS(w, visited, com_size, computers);
    }
  }
}

function solution(n, computers) {
  let answer = 0;
  const visited = new Array(n).fill(false);

  DFS(0, visited, n, computers);
  answer++;

  let index = visited.indexOf(false);
  while (index !== -1) {
    DFS(index, visited, n, computers);
    answer++;
    index = visited.indexOf(false);
  }

  return answer;
}
