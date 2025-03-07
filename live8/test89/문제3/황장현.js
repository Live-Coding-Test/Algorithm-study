function compare(a, b) {
  if (b.toString()[0] !== a.toString()[0])
    return b.toString()[0] - a.toString()[0];
  else {
  }
}

function solution(numbers) {
  numbers.sort((a, b) => compare(a, b));
  console.log(numbers);
}

console.log(solution([6, 10, 2, 11]));
// console.log(solution([3, 30, 34, 5, 9]));
