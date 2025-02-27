const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [K, N] = input[0];
  const lanList = input.slice(1);

  let low = 1;
  let high = Math.max(...lanList);
  let answer = 0;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let count = lanList.reduce((acc, cur) => acc + Math.floor(cur / mid), 0);

    if (count >= N) {
      answer = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return answer;
}

console.log(solution(input));
