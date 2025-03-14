const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const 특성값들 = input[1].sort((a, b) => a - b);

  let left = 0;
  let right = N - 1;
  let tempSum = Number.MAX_SAFE_INTEGER;
  let answer = '';

  while (left < right) {
    let sum = 특성값들[left] + 특성값들[right];

    if (tempSum > Math.abs(sum)) {
      tempSum = Math.abs(sum);
      answer = [특성값들[left], 특성값들[right]];
    }

    if (sum < 0) {
      left++;
    } else {
      right--;
    }
  }
  return answer.join(' ');
}

console.log(solution(input));
