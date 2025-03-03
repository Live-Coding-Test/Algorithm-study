const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const treeH = input[1].sort((a, b) => a - b);

  let start = 0;
  let end = treeH[treeH.length - 1];
  let answer = 0;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let sum = 0;

    for (let x of treeH) {
      if (x > mid) sum += x - mid;
    }

    if (sum >= M) {
      answer = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return answer;
}

console.log(solution(input));
