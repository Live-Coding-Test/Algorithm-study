const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, D] = input[0];
  const Info = input.slice(1);

  for (const [start, end, 지름길] of Info) {
    if (end > D) continue;
    if (end - start <= 지름길) continue;
    //
  }
}

console.log(solution(input));
