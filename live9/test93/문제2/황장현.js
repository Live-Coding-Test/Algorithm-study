const alphabetValues = {
  B: 1,
  C: 2,
  D: 3,
  E: 4,
  F: 5,
  G: 6,
  H: 7,
  I: 8,
  J: 9,
  K: 10,
  L: 11,
  M: 13,
  N: 12,
  O: 12,
  P: 11,
  Q: 10,
  R: 9,
  S: 8,
  T: 7,
  U: 6,
  V: 5,
  W: 4,
  X: 3,
  Y: 2,
  Z: 1,
};

function solution(name) {
  let answer = 0;
  for (let i = 0; i < name.length; i++) {
    if (name[i] === 'A') {
      answer += -1;
    } else {
      answer += alphabetValues[name[i]];
    }
  }
  answer += name.length;
  return answer;
}

// console.log(solution('JEROEN'));
// console.log(solution('JAAAN'));
// console.log(solution('JAAAKAN'));
console.log(solution('AAABAAAAB'));
