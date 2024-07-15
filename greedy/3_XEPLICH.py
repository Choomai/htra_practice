from dataclasses import dataclass

@dataclass
class Event:
    startDay: int
    endDay: int
    index: int
    duration: int

    def __init__(self, startDay, endDay, index) -> None:    
        self.startDay = startDay
        self.endDay = endDay
        self.index = index
        self.duration = endDay - startDay
    
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
total = 0
for event in events:
    print(event)
    if total + event.duration > N: break
    total += event.duration
    indexes.append(str(event.index))

with open("io/3_XEPLICH.out", "w") as f:
    f.write(str(total) + "\n")
    f.write(" ".join(indexes))