const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

function solution(input) {
  const N = input[0];
  if (N < 5) {
    return 0;
  }
  const chessBoard = Array.from({ length: N }, () => Array(N).fill(0));
  let count = 0;

  function back(chessBoard, posX, posY) {
    if (chessBoard[posY][posX] === 1) {
      return;
    }

    for (let i = 0; i < N; i++) {
      chessBoard[i][posX] = 1;
      chessBoard[posY][i] = 1;
      if (posY + i < N && posX + i < N) chessBoard[posY + i][posX + i] = 1;
      if (posY - i >= 0 && posX - i >= 0) chessBoard[posY - i][posX - i] = 1;
      if (posY - i >= 0 && posX + i < N) chessBoard[posY - i][posX + i] = 1;
      if (posY + i < N && posX - i >= 0) chessBoard[posY + i][posX - i] = 1;
    }

    for (let x = posX; x < N; x++) {
      for (let y = posY; y < N; y++) {
        if (chessBoard[y][x] !== 1) back(chessBoard, x, y);
      }
    }
  }

  back(chessBoard, 0, 0);
}

console.log(solution(input));
