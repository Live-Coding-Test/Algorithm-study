const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const arr = input[1].sort((a, b) => a - b);

  function getPermutation(arr, n) {
    if (n === 1) return arr.map((el) => [el]);

    let result = [];
    arr.forEach((element, idx, origin) => {
      let fixed = element;
      let rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
      const permutation = getPermutation(rest, n - 1);
      const attached = permutation.map((v) => [fixed, ...v]);
      result.push(...attached);
    });
    return result;
  }

  const answer = getPermutation(arr, M);

  answer.map((el) => console.log(el.join(' ')));
}

solution(input);
