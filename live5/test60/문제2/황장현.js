const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function solution(input) {
  const [N, GAME] = input[0];
  const memberList = input.slice(1).map((el) => el[0]);

  const ruleMap = {
    Y: 1,
    F: 2,
    O: 3,
  };
  const NUM = ruleMap[GAME];

  const uniqueMemberList = new Set(memberList);

  const result = Math.floor(uniqueMemberList.size / NUM);

  return result;
}

console.log(solution(input));
