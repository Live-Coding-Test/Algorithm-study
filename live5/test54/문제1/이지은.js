const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const n = Number(input[0]);
  const arr = input.slice(1);
  let answer = 0;

  let name = new Set();
  for (let i = 1; i < n; i++) {
    if (arr[i] === 'ENTER') {
      answer += name.size;
      name.clear();
    } else {
      name.add(arr[i]);
    }
  }
  return answer+=name.size;
}
console.log(solution(input));
