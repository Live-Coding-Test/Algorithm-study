const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];

  const result = [];
  function test(start, store) {
    if (store.length === M) {
      result.push(store.join(' '));
      return;
    }

    for (let i = start; i <= N; i++) {
      test(i + 1, [...store, i]);
    }
  }

  test(1, []);

  return result.join('\n');
}

console.log(solution(input));
