function solution(book_time) {
  const toMinutes = (time) => {
    const [hour, minute] = time.split(':').map(Number);
    return hour * 60 + minute;
  };

  book_time.sort((a, b) => toMinutes(a[0]) - toMinutes(b[0]));

  const rooms = [];

  for (const [start, end] of book_time) {
    const startTime = toMinutes(start);
    const endTime = toMinutes(end) + 10;

    let earliestRoomIndex = rooms.findIndex(
      (roomEndTime) => roomEndTime <= startTime
    );

    if (earliestRoomIndex !== -1) {
      rooms[earliestRoomIndex] = endTime;
    } else {
      rooms.push(endTime);
    }

    rooms.sort((a, b) => a - b);
  }

  return rooms.length;
}

console.log(
  solution([
    ['15:00', '17:00'],
    ['16:40', '18:20'],
    ['14:20', '15:20'],
    ['14:10', '19:20'],
    ['18:20', '21:20'],
  ])
);
