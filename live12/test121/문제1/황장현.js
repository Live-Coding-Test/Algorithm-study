const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

const [N, M, K] = input[0].split(' ').map(Number);
const jiminBoard = input.slice(1).map((el) => el.split(''));

const startBlack = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
const startWhite = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));

function calculateSum(board, start) {
  const height = jiminBoard.length;
  const width = jiminBoard[0].length;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      if ((i + j) % 2 === 0) {
        board[i + 1][j + 1] = jiminBoard[i][j] === start ? 1 : 0;
      } else {
        board[i + 1][j + 1] = jiminBoard[i][j] === start ? 0 : 1;
      }
    }
  }

  for (let i = 1; i <= height; i++) {
    for (let j = 1; j <= width; j++) {
      board[i][j] += board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1];
    }
  }
}

calculateSum(startBlack, 'B');
calculateSum(startWhite, 'W');

let minChanges = Infinity;
for (let i = K; i <= N; i++) {
  for (let j = K; j <= M; j++) {
    const blackSum =
      startBlack[i][j] -
      startBlack[i - K][j] -
      startBlack[i][j - K] +
      startBlack[i - K][j - K];
    const whiteSum =
      startWhite[i][j] -
      startWhite[i - K][j] -
      startWhite[i][j - K] +
      startWhite[i - K][j - K];
    minChanges = Math.min(minChanges, blackSum, whiteSum);
  }
}

console.log(minChanges);
