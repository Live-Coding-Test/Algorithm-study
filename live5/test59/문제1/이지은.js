const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));
function solution(input) {
  let answer = [];
  const [n] = input[0];
  const [m] = input[2];
  const arr = input[1];
  const section = input.slice(3);

  const addArr = Array(n).fill(0);
  addArr[0] = arr[0];

  for (let i = 1; i < n; i++) {
    addArr[i] = arr[i] + addArr[i - 1];
  }

  for (let k = 0; k < m; k++) {
    let temp = 0;
    let [i, j] = section[k];
    if (i === 1) {
      temp = addArr[j - 1];
    } else {
      temp = addArr[j - 1] - addArr[i - 2];
    }

    answer.push(temp);
  }
  return answer.join('\n');
}

console.log(solution(input));
