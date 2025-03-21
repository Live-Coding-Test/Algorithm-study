function solution(elements) {
  const n = elements.length;
  const sums = new Set();

  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < n; j++) {
      let sum = 0;
      for (let k = 0; k < i; k++) {
        sum += elements[(j + k) % n];
      }
      sums.add(sum);
    }
  }

  return sums.size;
}

console.log(solution([7, 9, 1, 1, 4]));
