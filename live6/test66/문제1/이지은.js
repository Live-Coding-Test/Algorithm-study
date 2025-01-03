const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((a) => a.split(' ').map(Number));

function solution(input) {
  const n = input[0][0];
  const arr = input.slice(1);
  const count = { '-1': 0, 0: 0, 1: 0 };

  function check(x, y, size) {
    const first = arr[x][y];
    for (let i = x; i < x + size; i++) {
      for (let j = y; j < y + size; j++) {
        if (arr[i][j] !== first) {
          return false;
        }
      }
    }
    return true;
  }

  function divide(x, y, size) {
    if (check(x, y, size)) {
      count[arr[x][y]]++;
    } else {
      const newSize = size / 3;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          divide(x + i * newSize, y + j * newSize, newSize);
        }
      }
    }
  }

  divide(0, 0, n);

  return `${count['-1']}\n${count['0']}\n${count['1']}`;
}

console.log(solution(input));
