function solution(skill, skill_trees) {
  let count = 0;

  skill_trees.forEach((tree) => {
    let filtered = tree
      .split('')
      .filter((s) => skill.includes(s))
      .join('');
    if (skill.startsWith(filtered)) count++;
  });

  return count;
}

console.log(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']));
