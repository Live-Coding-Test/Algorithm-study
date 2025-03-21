function solution(distance, rocks, n) {
  rocks.sort((a, b) => a - b);
  const temp = [0, ...rocks, distance];
  let left = 0;
  let right = distance;
  let answer = 0;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let prev = 0;
    let count = 0;

    for (const rock of temp) {
      if (rock - prev < mid) {
        count++;
        if (n < count) break;
      } else {
        prev = rock;
      }
    }

    if (n < count) {
      right = mid - 1;
    } else {
      answer = mid;
      left = mid + 1;
    }
  }

  return answer;
}

console.log(solution(25, [2, 14, 11, 21, 17], 2));
