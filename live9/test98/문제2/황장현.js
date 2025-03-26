const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function solution(input) {
  const digits = input.split('');
  const visited = Array(digits.length).fill(false);
  let found = Infinity;

  function dfs(current) {
    if (current.length === digits.length) {
      const num = parseInt(current.join(''), 10);
      if (num > parseInt(input, 10)) {
        found = Math.min(found, num);
      }
      return;
    }

    for (let i = 0; i < digits.length; i++) {
      if (!visited[i]) {
        visited[i] = true;
        current.push(digits[i]);
        dfs(current);
        current.pop();
        visited[i] = false;
      }
    }
  }

  dfs([]);

  return found === Infinity ? 0 : found;
}

console.log(solution(input));
