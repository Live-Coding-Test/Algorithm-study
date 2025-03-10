function solution(numbers) {
  numbers = numbers.map(String);

  numbers.sort((x, y) => (y + x).localeCompare(x + y));

  const answer = numbers.join('');

  return answer[0] === '0' ? '0' : answer;
}
console.log(solution([6, 10, 2, 11]));
// console.log(solution([3, 30, 34, 5, 9]));
