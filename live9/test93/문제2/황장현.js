function solution(name) {
  let moveCount = 0;
  let minMove = name.length - 1;

  for (let i = 0; i < name.length; i++) {
    const char = name[i];
    moveCount += Math.min(char.charCodeAt(0) - 65, 91 - char.charCodeAt(0));

    let nextIdx = i + 1;
    while (nextIdx < name.length && name[nextIdx] === 'A') {
      nextIdx++;
    }

    minMove = Math.min(
      minMove,
      i * 2 + (name.length - nextIdx),
      i + 2 * (name.length - nextIdx)
    );
  }

  return moveCount + minMove;
}

// console.log(solution('JEROEN'));
// console.log(solution('JAAAN'));
// console.log(solution('JAAAKAN'));
console.log(solution('AAABAAAAB'));
