const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function solution(input) {
  const T = Number(input[0][0]);
  let index = 1;
  const result = [];
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  for (let i = 0; i < T; i++) {
    const [H, W] = input[index].map((el) => Number(el));
    const sheeps = input
      .slice(index + 1, index + 1 + H)
      .map((row) => row.join('').split(''));

    index += H + 1;

    let count = 0;
    function dfs(x, y) {
      sheeps[x][y] = '.';
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx >= 0 && nx < H && ny >= 0 && ny < W && sheeps[nx][ny] === '#') {
          dfs(nx, ny);
        }
      }
    }

    for (let i = 0; i < H; i++) {
      for (let j = 0; j < W; j++) {
        if (sheeps[i][j] === '#') {
          count++;
          dfs(i, j);
        }
      }
    }
    result.push(count);
  }
  return result.join('\n');
}

console.log(solution(input));
