const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const 수열 = input[1];
  const x = input[2][0];
  수열.sort((a, b) => a - b);
  let start = 0;
  let end = N - 1;
  let answer = 0;
  while (start < end) {
    const isX = 수열[start] + 수열[end];
    if (isX === x) {
      answer++;
      start++;
      end--;
    } else if (isX > x) end--;
    else if (isX < x) start++;
  }

  return answer;
}

console.log(solution(input));
