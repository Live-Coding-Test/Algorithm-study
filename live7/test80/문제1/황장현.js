const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, K] = input[0];

  const visited = Array(100001).fill(false);

  if (N >= K) {
    return N - K;
  }

  const queue = [[N, 0]];
  visited[N] = true;

  while (queue.length) {
    const [X, time] = queue.shift();

    if (X === K) return time;

    if (X * 2 <= 100000 && !visited[X * 2]) {
      visited[X * 2] = true;
      queue.push([X * 2, time]);
    }
    if (X - 1 >= 0 && !visited[X - 1]) {
      visited[X - 1] = true;
      queue.push([X - 1, time + 1]);
    }
    if (X + 1 <= 100000 && !visited[X + 1]) {
      visited[X + 1] = true;
      queue.push([X + 1, time + 1]);
    }
  }
}

console.log(solution(input));
