const input = +require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function solution(input) {
  const roma = [1, 5, 10, 50];
  const store = new Set();

  function dfs(count, total, start) {
    if (count === input) {
      store.add(total);
      return;
    }

    for (let i = start; i < 4; i++) {
      dfs(count + 1, total + roma[i], i);
    }
  }

  dfs(0, 0, 0);

  return store.size;
}

console.log(solution(input));
