function solution(n, lost, reserve) {
  let 진짜두고온애들 = lost
    .filter((l) => !reserve.includes(l))
    .sort((a, b) => a - b);

  let 진짜빌려줄수있는애들 = reserve
    .filter((r) => !lost.includes(r))
    .sort((a, b) => a - b);

  let answer = n - 진짜두고온애들.length;

  for (let i = 0; i < 진짜두고온애들.length; i++) {
    const 진짜두고온애 = 진짜두고온애들[i];

    for (let j = 0; j < 진짜빌려줄수있는애들.length; j++) {
      const 진짜빌려줄수있는애 = 진짜빌려줄수있는애들[j];
      if (
        진짜빌려줄수있는애 === 진짜두고온애 - 1 ||
        진짜빌려줄수있는애 === 진짜두고온애 + 1
      ) {
        answer += 1;
        진짜빌려줄수있는애들[j] = -1;
        break;
      }
    }
  }
  return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
