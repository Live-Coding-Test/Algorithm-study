function solution(board) {
  const h = board.length;
  const w = board[0].length;
  const map = board.map((row) => row.split(""));

  let startX = -1;
  let startY = -1;

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (map[i][j] === "R") {
        startX = i;
        startY = j;
        break;
      }
    }
  }

  const visited = Array.from({ length: h }, () => Array(w).fill(false));
  visited[startX][startY] = true;

  const queue = [];
  queue.push([startX, startY]);

  while (queue.length) {
    const [x, y] = queue.shift();
    for (let dir = 0; dir < 4; dir++) {}
  }

  var answer = -1;
  return answer;
}
