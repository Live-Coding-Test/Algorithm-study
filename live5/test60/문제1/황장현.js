const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

/**
 * 참고
 */
function solution(input) {
  const textString = input[0][0];
  const M = parseInt(input[1][0], 10);
  const leftStack = [...textString];
  const rightStack = [];

  for (let i = 2; i < 2 + M; i++) {
    const [command, inputText] = input[i];

    if (command === 'L' && leftStack.length > 0) {
      rightStack.push(leftStack.pop());
    } else if (command === 'D' && rightStack.length > 0) {
      leftStack.push(rightStack.pop());
    } else if (command === 'B' && leftStack.length > 0) {
      leftStack.pop();
    } else if (command === 'P') {
      leftStack.push(inputText);
    }
  }

  return leftStack.concat(rightStack.reverse()).join('');
}

console.log(solution(input));
