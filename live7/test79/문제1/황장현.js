const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')

  .toString()

  .trim()

  .split('\n')

  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const storage = [];

  const dx = [-1, 1, 0, 0];

  const dy = [0, 0, -1, 1];

  function dfs(x, y, str, level) {
    if (x < 0 || x >= input.length || y < 0 || y >= input[x].length) return;

    str += input[x][y];

    if (level === 5) {
      if (!storage.includes(str)) storage.push(str);

      return;
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];

      const ny = y + dy[i];

      dfs(nx, ny, str, level + 1);
    }
  }

  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
      dfs(i, j, '', 0);
    }
  }

  return storage.length;
}

console.log(solution(input));

// 5개 갔을 떄, storage에 없다면 push
