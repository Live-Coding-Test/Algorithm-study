const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const T = input[0];
  let idx = 1;
  let result = [];
  for (let i = 0; i < T; i++) {
    const [N, M] = input[idx];
    const A = input[idx + 1];
    const B = input[idx + 2];
    A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
    let count = 0;
    const bMaxNum = Math.max(...B);

    for (let j = 0; j < N; j++) {
      if (A[j] > bMaxNum) {
        count += M;
        continue;
      }
      for (let k = 0; k < M; k++) {
        if (A[j] > B[k]) count++;
        else break;
      }
    }
    result.push(count);

    idx += 3;
  }
  return result.join('\n');
}

console.log(solution(input));

// 노가다로 풀었더니 이진탐색이랑 4배 차이 ㄷㄷ
// 배열에서 원하값 찾을 때 이진탐색 생각하기
