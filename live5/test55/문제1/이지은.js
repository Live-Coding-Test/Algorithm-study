const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  let answer = [];

  const testCase = input[0];
  const arr = input.slice(1);

  for (let i = 0; i < arr.length - 1; i += 2) {
    let num = 1;
    let [n, k] = arr[i].split(' ').map(Number);
    let importance = arr[i + 1]
      .split(' ')
      .map(Number)
      .sort((a, b) => b - a);
    let importanceArr = arr[i + 1]
      .split(' ')
      .map(Number)
      .map((el, idx) => [idx, el]);

    if (n === 1) {
      answer.push(1);
      continue;
    }

    while (importanceArr.length !== 0) {
      let max = Math.max(...importance);

      if (importanceArr[0][1] === max) {
        if (importanceArr[0][0] === k) {
          answer.push(num);
          break;
        }
        num++;

        importanceArr.shift();
        importance.shift();
      } else {
        let temp = importanceArr[0];
        importanceArr.shift();
        importanceArr = [...importanceArr, temp];
      }
    }
  }
  return answer.join('\n');
}

console.log(solution(input));
