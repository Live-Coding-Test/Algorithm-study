const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const A = input[1];
  const B = input[2];
  let p1 = 0;
  let p2 = 0;

  const result = [];

  while (p1 < N && p2 < M) {
    if (A[p1] < B[p2]) {
      result.push(A[p1++]);
    } else if (A[p1] > B[p2]) {
      result.push(B[p2++]);
    } else {
      result.push(A[p1], B[p2]);
      p1++;
      p2++;
    }
  }
  while (p1 < N) result.push(A[p1++]);
  while (p2 < M) result.push(B[p2++]);

  return result.join(' ');
}

console.log(solution(input));
