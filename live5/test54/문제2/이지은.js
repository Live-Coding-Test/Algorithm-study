const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const [n, x] = input[0].split(' ').map(Number);

  const arr = input[1].split(' ').map(Number);

  let max = arr.slice(0, x).reduce((a, b) => a + b);
  let answer = 1;

  let temp = max;
  for (let i = 1; i <= n - x; i++) {
    temp = temp + arr[i + x - 1] - arr[i - 1];
    if (temp > max) {
      max = temp;
      answer = 1;
    } else if (temp === max) {
      answer++;
    }
  }
  if (max === 0) console.log('SAD');
  else {
    console.log(max);
    console.log(answer);
  }
}

solution(input);
