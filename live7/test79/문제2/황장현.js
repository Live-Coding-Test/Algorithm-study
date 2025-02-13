const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M, K] = input[0];
  const 음식물쓰레기목록 = input.slice(1);
  const map = Array.from({ length: N }, () => Array(M).fill('.'));
  for (const [r, c] of 음식물쓰레기목록) {
    map[r - 1][c - 1] = '#';
  }

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  let answer = 0;
  let cnt = 0;

  function dfs(x, y) {
    if (x < 0 || x >= N || y < 0 || y >= M || map[x][y] === '.') return;
    map[x][y] = '.';
    cnt++;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      dfs(nx, ny, cnt);
    }
    answer = Math.max(answer, cnt);
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (map[i][j] === '#') {
        cnt = 0;
        dfs(i, j);
      }
    }
  }
  return answer;
}

console.log(solution(input));
