const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (arr[mid] === target) return 1;
    if (arr[mid] < target) start = mid + 1;
    else end = mid - 1;
  }

  return 0;
}

function solution(input) {
  const N = input[0][0];
  const cards = input[1];
  const M = input[2][0];
  const sangenCards = input[3];

  cards.sort((a, b) => a - b);

  const result = sangenCards.map((sangen) => binarySearch(cards, sangen));

  return result.join(' ');
}

console.log(solution(input));
