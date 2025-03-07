function solution(sequence, k) {
  let start = 0;
  let end = 0;
  let sum = sequence[0];
  let minLength = Infinity;
  let answer = [];

  while (end < sequence.length) {
    if (sum === k) {
      if (end - start < minLength) {
        minLength = end - start;
        answer = [start, end];
      }
      sum -= sequence[start++];
    } else if (sum < k) {
      end++;
      if (end < sequence.length) sum += sequence[end];
    } else {
      sum -= sequence[start++];
    }
  }

  return answer;
}

console.log(solution([1, 1, 1, 2, 3, 4, 5], 5));
