function solution(dirs) {
  let x = 0;
  let y = 0;

  const visited = new Set();
  const directions = {
    U: [0, 1],
    D: [0, -1],
    L: [-1, 0],
    R: [1, 0],
  };

  for (let dir of dirs) {
    const [dx, dy] = directions[dir];
    let nx = x + dx;
    let ny = y + dy;

    if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue;

    const path = `[${x},${y}]->[${nx},${ny}]`;

    visited.add(path);

    x = nx;
    y = ny;
  }

  return visited.size;
}

console.log(solution('ULURRDLLU'));
