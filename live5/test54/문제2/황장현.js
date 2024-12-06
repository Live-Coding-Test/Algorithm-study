const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, X] = input[0];
  const visitorCounts = input[1];

  let sum = 0;
  let max = 0;
  let count = 1;

  for (let i = 0; i < X; i++) {
    sum += visitorCounts[i];
  }
  max = sum;

  for (let i = 0; i < N - X; i++) {
    sum = sum - visitorCounts[i] + visitorCounts[i + X];
    if (max < sum) {
      max = sum;
      count = 1;
    } else if (max === sum) {
      count++;
    }
  }

  if (max === 0) {
    return 'SAD';
  } else {
    return `${max}\n${count}`;
  }
}

console.log(solution(input));
