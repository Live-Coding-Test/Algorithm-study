function solution(number, k) {
  let stack = [];
  let 제거할수 = k;

  for (let i = 0; i < number.length; i++) {
    while (
      제거할수 > 0 &&
      stack.length > 0 &&
      stack[stack.length - 1] < number[i]
    ) {
      stack.pop();
      제거할수--;
    }
    stack.push(number[i]);
  }

  while (제거할수 > 0) {
    stack.pop();
    제거할수--;
  }

  return stack.join('');
}

// console.log(solution('1924', 2));
// console.log(solution('1231234', 3));
// console.log(solution('4177252841', 4));
// console.log(solution('10', 1)); // 1
// console.log(solution('9876543214', 4)); // 987654
console.log(solution('333222111', 4)); // 33322
