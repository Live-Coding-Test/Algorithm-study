function solution(board, skill) {
  let count = 0;
  let effectMap = Array.from({ length: board.length + 1 }, () =>
    Array(board[0].length + 1).fill(0)
  );

  for (let i = 0; i < skill.length; ++i) {
    const [skillType, r1, c1, r2, endCol, degree] = skill[i];
    const adjustedImpact = skillType === 1 ? -degree : degree;

    effectMap[r1][c1] += adjustedImpact;
    effectMap[r1][endCol + 1] -= adjustedImpact;
    effectMap[r2 + 1][c1] -= adjustedImpact;
    effectMap[r2 + 1][endCol + 1] += adjustedImpact;
  }

  for (let i = 0; i < board.length; ++i) {
    for (let j = 0; j < board[i].length; ++j) {
      if (i > 0) effectMap[i][j] += effectMap[i - 1][j];
      if (j > 0) effectMap[i][j] += effectMap[i][j - 1];
      if (i > 0 && j > 0) effectMap[i][j] -= effectMap[i - 1][j - 1];
    }
  }

  for (let i = 0; i < board.length; ++i) {
    for (let j = 0; j < board[i].length; ++j) {
      board[i][j] += effectMap[i][j];
      if (board[i][j] > 0) {
        count++;
      }
    }
  }

  return count;
}

console.log(
  solution(
    [
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
    ],
    [
      [1, 0, 0, 3, 4, 4],
      [1, 2, 0, 2, 3, 2],
      [2, 1, 0, 3, 1, 2],
      [1, 0, 1, 3, 3, 1],
    ]
  )
);
