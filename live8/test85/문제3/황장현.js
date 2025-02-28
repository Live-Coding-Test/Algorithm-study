function solution(clothes) {
  let answer = 1;
  const dic = {};

  for (let i = 0; i < clothes.length; i++) {
    const kind = clothes[i][1];
    if (dic[kind] !== undefined) {
      dic[kind] += 1;
    } else {
      dic[kind] = 1;
    }
  }

  for (let k in dic) {
    answer *= dic[k] + 1;
  }

  answer -= 1;
  return answer;
}

console.log(
  solution([
    ['yellow_hat', 'headgear'],
    ['blue_sunglasses', 'eyewear'],
    ['green_turban', 'headgear'],
  ])
);
