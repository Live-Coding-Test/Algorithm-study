function solution(answers) {
  let stu1 = [1, 2, 3, 4, 5];
  let stu2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let cnt = [0, 0, 0];
  let ans = [];

  for (let i = 0; i < answers.length; i++) {
    if (stu1[i % stu1.length] === answers[i]) {
      cnt[0]++;
    }
    if (stu2[i % stu2.length] === answers[i]) {
      cnt[1]++;
    }
    if (stu3[i % stu3.length] === answers[i]) {
      cnt[2]++;
    }
  }
  const maxCollect = Math.max(...cnt);
  for (let i = 0; i < cnt.length; i++) {
    if (cnt[i] === maxCollect) {
      ans.push(i + 1);
    }
  }

  return ans;
}

console.log(solution([1, 2, 3, 4, 5]));
