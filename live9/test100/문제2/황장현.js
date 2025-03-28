const input = +require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function solution(input) {
  const N = input;
  let count = 0;

  function backTrack(y, x, idx, map) {
    if (idx === N) {
      count++;
      return;
    }

    for (let i = 0; i < N; i++) {
      map[y][i] = 1;
      map[i][x] = 1;
      if (y + i < N && x + i < N) map[y + i][x + i] = 1;
      if (y - i >= 0 && x - i >= 0) map[y - i][x - i] = 1;
      if (y + i < N && x - i >= 0) map[y + i][x - i] = 1;
      if (y - i >= 0 && x + i < N) map[y - i][x + i] = 1;
    }

    for (let i = 0; i < N; i++) {
      const nextY = y + 1;
      if (nextY < N && map[nextY][i] === 0) backTrack(nextY, i, idx + 1, map);
      else break;
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const chessMap = Array.from({ length: N }, () => Array(N).fill(0));
      backTrack(i, j, 1, chessMap);
    }
  }
  return count;
}

console.log(solution(input));
