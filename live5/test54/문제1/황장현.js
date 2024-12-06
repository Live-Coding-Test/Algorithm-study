const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function solution(input) {
  const N = Number(input[0][0]);
  let nickCounts = 0;

  let dupNick = new Set();

  for (let i = 1; i <= N; i++) {
    const log = input[i][0];
    if (log === 'ENTER') {
      dupNick.clear();
    } else if (!dupNick.has(log)) {
      nickCounts++;
      dupNick.add(log);
    }
  }
  return nickCounts;
}

console.log(solution(input));
