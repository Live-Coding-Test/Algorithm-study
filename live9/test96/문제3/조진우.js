function solution(elements) {
  var answer = 0;
  for (let i = 1; i <= elements.length; i++) {
    for (let j = 0; j < elements.length; j++) {
      const subArr = [];
      for (let k = 0; k < i; k++) {
        subArr.push(elements[(j + k) % n]);
      }
    }
  }
  return answer;
}

console.log(solution([7, 9, 1, 1, 4]));
