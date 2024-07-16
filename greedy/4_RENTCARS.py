# Identical to TTH/18-19/1
from dataclasses import dataclass

@dataclass
class SelectedCar:
    group: int
    consume_rate: int
    index: int


with open("io/4_RENTCARS.inp", "r") as f:
    N, M = map(int, f.readline().split(" "))
    groups = list(map(int, f.readline().split(" ")))
    consume_rate = list(map(int, f.readline().split(" ")))

sorted_group = sorted(groups)
sorted_consume_rate = sorted(consume_rate, reverse=True)


with open("io/4_RENTCARS.out", "w") as f:
    pass