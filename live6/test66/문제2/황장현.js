const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const map = input.slice(1);

  const visited = Array.from({ length: N }, () => Array(N).fill(false));

  function jumpKing(x, y) {
    const movePoint = map[x][y];

    if (movePoint === -1) return true;

    if (visited[x][y]) return false;

    visited[x][y] = true;

    const goRightOrDown = [
      [x + movePoint, y],
      [x, y + movePoint],
    ];

    for (const [nextX, nextY] of goRightOrDown) {
      if (nextX < N && nextY < N) {
        if (jumpKing(nextX, nextY)) return true;
      }
    }

    return false;
  }

  return jumpKing(0, 0) ? 'HaruHaru' : 'Hing';
}

console.log(solution(input));
