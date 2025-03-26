const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const N = input[0][0];
  const An = input[1];
  const 연산자수 = input[2];

  let maxResult = -Infinity;
  let minResult = Infinity;

  function dfs(currentIndex, total, plus, minus, multiply, divide) {
    if (currentIndex === An.length) {
      maxResult = Math.max(maxResult, total);
      minResult = Math.min(minResult, total);
      return;
    }

    const currentNum = An[currentIndex];

    if (plus > 0) {
      dfs(
        currentIndex + 1,
        total + currentNum,
        plus - 1,
        minus,
        multiply,
        divide
      );
    }

    if (minus > 0) {
      dfs(
        currentIndex + 1,
        total - currentNum,
        plus,
        minus - 1,
        multiply,
        divide
      );
    }

    if (multiply > 0) {
      dfs(
        currentIndex + 1,
        total * currentNum,
        plus,
        minus,
        multiply - 1,
        divide
      );
    }

    if (divide > 0) {
      const result =
        total < 0
          ? -Math.floor(Math.abs(total) / currentNum)
          : Math.floor(total / currentNum);

      dfs(currentIndex + 1, result, plus, minus, multiply, divide - 1);
    }
  }

  dfs(1, An[0], ...연산자수);
  const result = [];
  result.push(maxResult);
  result.push(minResult);

  return result.join('\n');
}

console.log(solution(input));
