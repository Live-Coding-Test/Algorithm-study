function solution(name) {
  let nameArr = name.split("");
  let currentValue = "A";
  let totalCount = 0;

  for (let i = 0; i < nameArr.length; i++) {
    let upDownCount = 0;
    let leftRightCount = 0;

    upDownCount = Number(
      Math.min(
        Math.abs(nameArr[i].charCodeAt(0) - currentValue.charCodeAt(0)),
        26 - Math.abs(nameArr[i].charCodeAt(0) - currentValue.charCodeAt(0))
      )
    );

    leftRightCount = i;

    totalCount += Math.max(upDownCount, leftRightCount);
    currentValue = nameArr[i];
  }

  return totalCount;
}

console.log(solution("JEROEN"));
