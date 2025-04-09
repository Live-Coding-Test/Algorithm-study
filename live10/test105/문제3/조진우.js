function solution(order) {
  const containerBelt = [];
  let now = 1;
  let count = 0;

  for (let i = 0; i < order.length; i++) {
    const target = order[i];

    console.log(target);

    while (now <= order.length && now !== target) {
      containerBelt.push(now);
      now++;
    }
    console.log("belt:", containerBelt);

    if (now === target) {
      count++;
      now++;
    } else if (containerBelt.length && containerBelt[0] === target) {
      containerBelt.shift();
      count++;
    } else {
      break;
    }

    console.log("--------------");
  }

  return count;
}

console.log(solution([4, 3, 1, 2, 5])); // 출력: 2
