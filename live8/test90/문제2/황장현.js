const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];

  const temp = new Set();
  const result = [];
  function test(start, store) {
    if (store.length === M) {
      result.push(store);
      temp.add(store.sort((a, b) => a - b));
      return;
    }
    if (temp.has(store.sort((a, b) => a - b))) {
      return;
    }
    for (let i = start; i <= N; i++) {
      test(i, [...store, i]);
    }
  }

  test(1, []);
}

console.log(solution(input));
