function solution(n) {
  let ways = 0;
  let startNum = 1;
  while (startNum <= n) {
    let sum = 0;
    let i = startNum;
    while (true) {
      sum = sum + i;
      if (sum === n) {
        ways++;
        break;
      }
      if (sum > n) break;
      i++;
    }
    startNum++;
  }
  return ways;
}

console.log(solution(15));
