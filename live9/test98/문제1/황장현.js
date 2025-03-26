const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const numArr = [0, ...input[1]];

  function bF(idx, sec, size) {
    if (sec > M) return 0;
    if (sec === M || idx >= N) return size;

    let ans = 0;
    ans = Math.max(
      idx + 1 <= N ? bF(idx + 1, sec + 1, size + numArr[idx + 1]) : 0,
      idx + 2 <= N
        ? bF(idx + 2, sec + 1, Math.floor(size / 2) + numArr[idx + 2])
        : 0
    );

    return ans;
  }

  return bF(0, 0, 1);
}

console.log(solution(input));
