function solution(stones, k) {
  let min = 1;
  let max = 200000000;

  while (min <= max) {
    const mid = Math.floor((min + max) / 2);
    let cnt = 0;
    for (let stone of stones) {
      if (stone - mid <= 0) cnt++;
      else cnt = 0;

      if (cnt === k) break;
    }
    if (cnt === k) max = mid - 1;
    else min = mid + 1;
  }
  return min;
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
