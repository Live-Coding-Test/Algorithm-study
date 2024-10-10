const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [K, N] = input[0];
  const lanCables = input.slice(1);

  let lowLanCableLength = 1;
  let highLanCableLength = Math.max(...lanCables);
  let result = 0;

  while (lowLanCableLength <= highLanCableLength) {
    const midLanCableLength = Math.floor(
      (lowLanCableLength + highLanCableLength) / 2
    );

    let count = lanCables.reduce(
      (sum, lanCable) => sum + Math.floor(lanCable / midLanCableLength),
      0
    );

    if (count >= N) {
      result = midLanCableLength;
      lowLanCableLength = midLanCableLength + 1;
    } else {
      highLanCableLength = midLanCableLength - 1;
    }
  }

  return result;
}

console.log(solution(input));
