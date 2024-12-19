function solution(maps) {
  const selo = maps.length;
  const galo = maps[0].length;
  const visited = Array.from({ length: selo }, () => Array(galo).fill(false));
  const result = [];

  function dfs(x, y) {
    if (
      x < 0 ||
      x >= selo ||
      y < 0 ||
      y >= galo ||
      maps[x][y] === 'X' ||
      visited[x][y]
    ) {
      return 0;
    }

    visited[x][y] = true;
    let sum = Number(maps[x][y]);
    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];

    for (const [dx, dy] of directions) {
      sum += dfs(x + dx, y + dy);
    }

    return sum;
  }

  for (let i = 0; i < selo; i++) {
    for (let j = 0; j < galo; j++) {
      if (!visited[i][j] && maps[i][j] !== 'X') {
        result.push(dfs(i, j));
      }
    }
  }
  if (result.length === 0) result.push(-1);

  return result.sort((a, b) => a - b);
}

// console.log(solution(['X591X', 'X1X5X', 'X231X', '1XXX1']));
console.log(solution(['XXX', 'XXX', 'XXX']));
