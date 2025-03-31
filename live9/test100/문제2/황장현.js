const input = +require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function solution(N) {
  let count = 0;
  const column = Array(N).fill(false);
  const diagonal1 = Array(2 * N - 1).fill(false);
  const diagonal2 = Array(2 * N - 1).fill(false);

  function backTrack(row) {
    if (row === N) {
      count++;
      return;
    }

    for (let col = 0; col < N; col++) {
      if (
        column[col] ||
        diagonal1[row + col] ||
        diagonal2[row - col + (N - 1)]
      ) {
        continue;
      }

      column[col] = true;
      diagonal1[row + col] = true;
      diagonal2[row - col + (N - 1)] = true;

      backTrack(row + 1);

      column[col] = false;
      diagonal1[row + col] = false;
      diagonal2[row - col + (N - 1)] = false;
    }
  }

  backTrack(0);
  return count;
}

console.log(solution(input));
