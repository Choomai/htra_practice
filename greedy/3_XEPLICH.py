from dataclasses import dataclass

@dataclass
class Event:
    startDay: int
    endDay: int
    index: int

    def __eq__(self, other: object) -> bool:
        return self.endDay == other.endDay
    def __ne__(self, other: object) -> bool:
        return self.endDay != other.endDay
    def __lt__(self, other: object) -> bool:
        return self.endDay < other.endDay
    def __gt__(self, other: object) -> bool:
        return self.endDay > other.endDay
    def __le__(self, other: object) -> bool:
        return self.endDay <= other.endDay
    def __ge__(self, other: object) -> bool:
        return self.endDay >= other.endDay

events = []
with open("io/3_XEPLICH.inp", "r") as f:
    N = int(f.readline())
    startDays = list(map(int, f.readline().split(" ")))
    endDays = list(map(int, f.readline().split(" ")))

    for i in range(N):
        events.append(Event(startDays[i], endDays[i], i))

events = sorted(events)
indexes = []
last_event = 0
for event in events:
    if last_event >= event.startDay: continue
    last_event = event.endDay
    indexes.append(str(event.index + 1))

with open("io/3_XEPLICH.out", "w") as f:
    f.write(str(len(indexes)) + "\n")
    f.write(" ".join(indexes))