const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const elemets = input
    .slice(1)
    .flat()
    .sort((a, b) => a - b);

  let answer = 4;

  for (let i = 0; i < N; i++) {
    let start = i;
    let end = N - 1;

    while (start < end) {
      if (elemets[end] - elemets[start] > 4) {
        end--;
      } else {
        const temp = 4 - (end - start);
        answer = Math.min(answer, temp);
        break;
      }
    }
  }

  return answer;
}

console.log(solution(input));
