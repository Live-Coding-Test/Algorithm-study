const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

const S = input[0];
const P = input[1];

let index = 0;
let count = 0;

while (index < P.length) {
  let maxLen = 0;

  for (let j = 0; j < S.length; j++) {
    let temp = 0;
    while (
      index + temp < P.length &&
      j + temp < S.length &&
      P[index + temp] === S[j + temp]
    ) {
      temp++;
    }
    if (temp > maxLen) {
      maxLen = temp;
    }
  }

  index += maxLen;
  count++;
}

console.log(count);
