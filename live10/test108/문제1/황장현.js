const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

const parts = input.split('-');

let result = parts[0].split('+').reduce((acc, num) => acc + parseInt(num), 0);

for (let i = 1; i < parts.length; i++) {
  const sum = parts[i].split('+').reduce((acc, num) => acc + parseInt(num), 0);
  result -= sum;
}

console.log(result);
