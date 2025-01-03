const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((a) => a.split(' ').map(Number));

function solution(input) {
  const n = input[0][0];
  const arr = input.slice(1);
  const visited = Array.from({ length: n }, () => Array(n).fill(false));

  const directions = [
    [0, 1],
    [1, 0],
  ];

  let isReachable = false;

  function dfs(x, y) {
    if (x === n - 1 && y === n - 1) {
      isReachable = true;
      return;
    }

    visited[x][y] = true;
    const step = arr[x][y];

    for (const [dx, dy] of directions) {
      const nx = x + dx * step;
      const ny = y + dy * step;

      if (
        nx >= 0 &&
        ny >= 0 &&
        nx < n &&
        ny < n &&
        !visited[nx][ny] &&
        arr[nx][ny] !== 0
      ) {
        dfs(nx, ny);
      }
    }
  }

  dfs(0, 0);

  return isReachable ? 'HaruHaru' : 'Hing';
}

console.log(solution(input));
