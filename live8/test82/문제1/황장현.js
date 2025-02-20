const fs = require('fs');

const input = fs
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [n, m] = input[0];
  const drawing = input.slice(1).map((row) => [...row]);

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  let count = 0;
  let maxSize = 0;

  function dfs(x, y) {
    let size = 1;
    drawing[x][y] = 0;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx >= 0 && nx < n && ny >= 0 && ny < m && drawing[nx][ny] === 1) {
        size += dfs(nx, ny);
      }
    }
    return size;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (drawing[i][j] === 1) {
        count++;
        maxSize = Math.max(maxSize, dfs(i, j));
      }
    }
  }

  console.log(count);
  console.log(maxSize);
}

solution(input);
