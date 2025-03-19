function solution(routes) {
  routes.sort((a, b) => a[1] - b[1]);

  let cameraCount = 0;
  let lastCameraPos = -30001;

  for (let route of routes) {
    let [enter, exit] = route;

    if (enter > lastCameraPos) {
      cameraCount++;
      lastCameraPos = exit;
    }
  }

  return cameraCount;
}

console.log(
  solution([
    [-20, -15],
    [-14, -5],
    [-18, -13],
    [-5, -3],
  ])
);
