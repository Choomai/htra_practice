from dataclasses import dataclass
from pprint import pprint

@dataclass
class Car:
    consume_rate: int
    distance: int
    index: int

    def __lt__(self, other: object) -> bool:
        return self.consume_rate < other.consume_rate
    def __gt__(self, other: object) -> bool:
        return self.consume_rate > other.consume_rate

@dataclass
class Group:
    index: int

with open("io/ENEGRY.inp", "r") as f:
    n, m = map(int, f.readline().split())
    distances = list(map(int, f.readline().split()))
    consume_rates = []
    org_consume_rates = []
    for index, consume_rate in enumerate(map(int, f.readline().split())):
        consume_rates.append(Car(consume_rate, -1, index))
        org_consume_rates.append(consume_rate)

consume_rates = sorted(consume_rates)
sorted_distances = sorted(distances)
chosen_car = []

for index, distance in enumerate(sorted_distances):
    consume_rates[index].distance = distance
    consume_rate_index = org_consume_rates.index(consume_rates[index].consume_rate)
    
    chosen_car.append(consume_rate_index+1)
    org_consume_rates[consume_rate_index] = -1

pprint(chosen_car)