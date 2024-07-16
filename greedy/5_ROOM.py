from dataclasses import dataclass

tests = []
indexes = []

@dataclass
class Test:
    start: int
    end: int
    index: int

    def __lt__(self, other: object) -> bool:
        if self.end == other.end: return self.start < other.start
        else: return self.end < other.end
    def __gt__(self, other: object) -> bool:
        if self.end == other.end: return self.start > other.start
        else: return self.end > other.end

with open("io/5_ROOM.inp", "r") as f:
    N = int(f.readline())
    for i in range(N): tests.append(Test(*map(int, f.readline().split(" ")), i))

tests = sorted(tests)
indexes = []
last_test = -1
for test in tests:
    if last_test >= test.start: continue
    last_test = test.end
    indexes.append(str(test.index + 1))

with open("io/5_ROOM.out", "w") as f:
    f.write(f"{len(indexes)}\n")
    f.writelines(" ".join(indexes))