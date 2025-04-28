const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function canTransform(S, T) {
  function dfs(current) {
    if (current.length < S.length) return false;
    if (current === S) return true;

    let result = false;

    if (current[current.length - 1] === 'A') {
      result = result || dfs(current.slice(0, -1));
    }

    if (current[0] === 'B') {
      const reversed = current.slice(1).split('').reverse().join('');
      result = result || dfs(reversed);
    }

    return result;
  }

  return dfs(T) ? 1 : 0;
}

function solution(input) {
  const S = input[0][0];
  const T = input[1][0];

  console.log(canTransform(S, T));
}

solution(input);
