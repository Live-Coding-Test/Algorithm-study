function solution(x, y, n) {
  const visited = new Set([x]);
  const queue = [[x, 0]];
  let queueIndex = 0;

  while (queueIndex < queue.length) {
    const [current, count] = queue[queueIndex++];
    if (current === y) return count;

    const calculate = [current + n, current * 2, current * 3];

    for (const cal of calculate) {
      if (cal <= y && !visited.has(cal)) {
        visited.add(cal);
        queue.push([cal, count + 1]);
      }
    }
  }

  return -1;
}

console.log(solution(10, 40, 30));
