const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const n = input[0];
  const arr = input.slice(1).map((el) => el.split(' '));
  let answer = [];
  let people = new Map();
  for ([person, state] of arr) {
    people.set(person, (people.has(person) ? people.get(person) : 0) + 1);
  }

  for (let x of people) {
    if (x[1] % 2 !== 0) {
      answer.push(x[0]);
    }
  }
  return answer.sort().reverse().join('\n');
}

console.log(solution(input));
