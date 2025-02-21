const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

const LIMIT = 1299709;
const isPrime = Array(LIMIT + 1).fill(true);
isPrime[0] = isPrime[1] = false;
const primes = [];

for (let i = 2; i <= LIMIT; i++) {
  if (isPrime[i]) {
    primes.push(i);
    for (let j = i * 2; j <= LIMIT; j += i) {
      isPrime[j] = false;
    }
  }
}

function solution(input) {
  const T = input[0];
  const list = input.slice(1);
  const result = [];

  for (let numb of list) {
    if (isPrime[numb]) {
      result.push(0);
      continue;
    }

    let left = 0,
      right = primes.length - 1;
    while (left < right) {
      let mid = Math.floor((left + right) / 2);
      if (primes[mid] >= numb) right = mid;
      else left = mid + 1;
    }

    let prevPrime = primes[left - 1];
    let nextPrime = primes[left];

    result.push(nextPrime - prevPrime);
  }
  return result.join('\n');
}

console.log(solution(input));
