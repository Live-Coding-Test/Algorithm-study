const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const paper = input.slice(1);

  let minus = 0;
  let zero = 0;
  let plus = 0;

  function check(board, n) {
    const firstValue = board[0][0];
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] !== firstValue) {
          return false;
        }
      }
    }

    if (firstValue === -1) minus++;
    else if (firstValue === 0) zero++;
    else if (firstValue === 1) plus++;

    return true;
  }

  function divideNine(board, n) {
    if (check(board, n)) return;

    const size = n / 3;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        const subPaper = board
          .slice(i * size, (i + 1) * size)
          .map((row) => row.slice(j * size, (j + 1) * size));

        divideNine(subPaper, size);
      }
    }
  }

  divideNine(paper, N);
  const result = [];
  result.push(minus);
  result.push(zero);
  result.push(plus);

  return result.join('\n');
}

console.log(solution(input));
