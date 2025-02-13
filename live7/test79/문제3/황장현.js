const 사전 = {
  A: 1,
  B: 2,
  C: 3,
  D: 4,
  E: 5,
  F: 6,
  G: 7,
  H: 8,
  I: 9,
  J: 10,
  K: 11,
  L: 12,
  M: 13,
  N: 14,
  O: 15,
  P: 16,
  Q: 17,
  R: 18,
  S: 19,
  T: 20,
  U: 21,
  V: 22,
  W: 23,
  X: 24,
  Y: 25,
  Z: 26,
};

function solution(msg) {
  const result = [];
  while (msg.length > 0) {
    let word = msg[0];
    let idx = 1;
    while (사전[word + msg[idx]] !== undefined) {
      word += msg[idx];
      idx++;
    }
    result.push(사전[word]);
    사전[word + msg[idx]] = Object.keys(사전).length + 1;
    msg = msg.slice(idx);
  }
  return result;
}

console.log(solution('KAKAO')); // [11, 1, 27, 15]
