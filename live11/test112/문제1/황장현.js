const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function generateAnagrams(word) {
  const chars = word.split('').sort();
  const used = Array(chars.length).fill(false);
  const result = [];
  const path = [];

  function backtrack() {
    if (path.length === chars.length) {
      result.push(path.join(''));
      return;
    }

    for (let i = 0; i < chars.length; i++) {
      if (used[i]) continue;
      if (i > 0 && chars[i] === chars[i - 1] && !used[i - 1]) continue;

      used[i] = true;
      path.push(chars[i]);

      backtrack();

      path.pop();
      used[i] = false;
    }
  }

  backtrack();
  return result;
}

function solution(input) {
  const N = input[0][0];
  const words = input.slice(1).map((el) => el[0]);
  const output = [];

  for (let i = 0; i < N; i++) {
    const anagrams = generateAnagrams(words[i]);
    output.push(...anagrams);
  }
  console.log(output.join('\n'));
}

solution(input);
