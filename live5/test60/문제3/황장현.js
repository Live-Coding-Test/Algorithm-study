function solution(s) {
  const originalLength = s.length;
  const withoutZeros = s.replace(/0/g, '');
  const zeroCount = originalLength - withoutZeros.length;
}

console.log(solution('01110'));
