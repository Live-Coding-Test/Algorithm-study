function solution(order) {
  const stack = [];
  let result = 0;
  let current = 1;

  for (let i = 0; i < order.length; i++) {
    while (
      current <= order.length &&
      (stack.length === 0 || stack[stack.length - 1] !== order[i])
    ) {
      stack.push(current);
      current++;
    }
    if (stack[stack.length - 1] === order[i]) {
      stack.pop();
      result++;
    } else {
      break;
    }
  }

  return result;
}

console.log(solution([4, 3, 1, 2, 5]));
