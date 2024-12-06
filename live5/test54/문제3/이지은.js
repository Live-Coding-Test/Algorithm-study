function solution(n, lost, reserve) {
  let realLost = lost
    .filter((el) => !reserve.includes(el))
    .sort((a, b) => a - b);

  let realReserve = reserve
    .filter((el) => !lost.includes(el))
    .sort((a, b) => a - b);

  let answer = n - realLost.length;

  for (let i = 0; i < realLost.length; i++) {
    for (let j = 0; j < realReserve.length; j++) {
      if (realLost[i] - 1 === realReserve[j]) {
        answer++;
        realReserve.splice(j, 1);
        break;
      } else if (realLost[i] + 1 === realReserve[j]) {
        answer++;
        realReserve.splice(j, 1);
        break;
      }
    }
  }

  return answer;
}

// console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [4, 2], [3, 5]));
