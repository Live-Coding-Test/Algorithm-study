function solution(n) {
  const triangle = Array.from({ length: n }, (_, i) => Array(i + 1).fill(0));
  const total = (n * (n + 1)) / 2;

  const dx = [1, 0, -1];
  const dy = [0, 1, -1];

  let x = 0,
    y = 0,
    dir = 0,
    num = 1;

  while (num <= total) {
    triangle[x][y] = num++;
    let nx = x + dx[dir];
    let ny = y + dy[dir];

    if (nx < 0 || ny < 0 || nx >= n || ny > nx || triangle[nx][ny] !== 0) {
      dir = (dir + 1) % 3;
      nx = x + dx[dir];
      ny = y + dy[dir];
    }

    x = nx;
    y = ny;
  }

  return triangle.flat();
}

console.log(solution(4));
