function solution(board, skill) {
  let currentBoard = board;

  for (let i = 0; i < skill.length; i++) {
    for (let j = skill[i][1]; j <= skill[i][3]; j++) {
      for (let k = skill[i][2]; k <= skill[i][4]; k++) {
        if (skill[i][0] === 1) {
          currentBoard[j][k] -= skill[i][5];
        }
        if (skill[i][0] === 2) {
          currentBoard[j][k] += skill[i][5];
        }
      }
    }
  }

  let count = 0;
  for (let j = 0; j < board.length; j++) {
    for (let k = 0; k < board[0].length; k++) {
      if (currentBoard[j][k] > 0) count++;
    }
  }

  return count;
}

console.log(
  solution(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    [
      [1, 1, 1, 2, 2, 4],
      [1, 0, 0, 1, 1, 2],
      [2, 2, 0, 2, 0, 100],
    ]
  )
);
