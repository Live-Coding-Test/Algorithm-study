function solution(n, lost, reserve) {
  for (const haveStudent of reserve) {
    if (lost.indexOf(haveStudent - 1) !== -1) {
      continue;
    }
    if (lost.indexOf(haveStudent + 1) !== -1) {
    }
  }
}

console.log(solution(5, [2, 4], [1, 3, 5]));
