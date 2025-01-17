const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

function solution(input) {
  const [n, m] = input;

  let arr = Array.from({ length: n }, (_, idx) => idx + 1);

  let answer = [];
  function permutation(tempArr, used) {
    if (tempArr.length === m) {
      answer.push([...tempArr]);
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (!used[i]) {
        used[i] = true;
        permutation([...tempArr, arr[i]], used);
        used[i] = false;
      }
    }
  }

  permutation([], Array(n).fill(false));
  return answer.map((x) => x.join(' ')).join('\n');
}
console.log(solution(input));
