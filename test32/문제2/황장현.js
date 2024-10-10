const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function binarySearch(target, arr) {
  let low = 0;
  let high = arr.length;

  while (low < high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid;
    }
  }

  return low;
}

function solution(input) {
  const T = input[0][0];
  const result = [];

  for (let i = 1; i < input.length; i += 3) {
    const [N, M] = input[i];
    const aSizes = input[i + 1];
    const bSizes = input[i + 2];

    aSizes.sort((a, b) => a - b);
    bSizes.sort((a, b) => a - b);

    let count = 0;

    for (let j = 0; j < N; j++) {
      count += binarySearch(aSizes[j], bSizes);
    }

    result.push(count);
  }
  return result.join('\n');
}

console.log(solution(input));
