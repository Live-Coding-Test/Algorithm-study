const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const A = input[1];

  let answer = 0;
  for (let i = 0; i < N; i++) {
    let p1 = i;
    let sum = 0;

    while (p1 < N) {
      sum += A[p1];

      if (sum === M) {
        answer++;
        break;
      }
      if (sum > M) {
        break;
      }
      p1++;
    }
  }
  return answer;
}

console.log(solution(input));
