const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

const [N, M, K] = input[0].split(' ').map(Number);
const board = input.slice(1).map((el) => el[0].split(''));

const sumB = Array.from({ length: N }, () => Array(M).fill(0));
const sumW = Array.from({ length: N }, () => Array(M).fill(0));
console.log(sumB);

function calculateSum(board, sum, start) {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      let count = 0;
      if ((i + j) % 2 === 0) {
        count = board[i][j] === start ? 1 : 0;
      } else {
        count = board[i][j] === start ? 0 : 1;
      }
      sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + count;
    }
  }
}

calculateSum(board, sumB, 'B');
calculateSum(board, sumW, 'W');
