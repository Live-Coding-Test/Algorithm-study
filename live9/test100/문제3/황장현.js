function solution(queue1, queue2) {
  let sum1 = queue1.reduce((acc, cur) => acc + cur, 0);
  let sum2 = queue2.reduce((acc, cur) => acc + cur, 0);

  let count = 0;
  let maxOperations = queue1.length * 3;

  let idx1 = 0;
  let idx2 = 0;
  let totalQueue = [...queue1, ...queue2];

  while (sum1 !== sum2) {
    if (count > maxOperations) return -1;

    if (sum1 < sum2) {
      const popNum = totalQueue[idx2 + queue1.length];
      sum2 -= popNum;
      sum1 += popNum;
      idx2++;
    } else {
      const popNum = totalQueue[idx1];
      sum1 -= popNum;
      sum2 += popNum;
      idx1++;
    }
    count++;
  }

  return count;
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]));
console.log(solution([1, 2, 1, 2], [1, 10, 1, 2]));
