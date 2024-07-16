# Identical to TTH/18-19/1
from dataclasses import dataclass

@dataclass
class SelectedCar:
    distance: int
    consume_rate: int
    index: int
    order: int

    def __lt__(self, other: object) -> bool:
        return self.order < other.order
    def __gt__(self, other: object) -> bool:
        return self.order > other.order
    def __le__(self, other: object) -> bool:
        return self.order <= other.order
    def __ge__(self, other: object) -> bool:
        return self.order <= other.order

    def get_cost(self) -> int:
        return self.distance * self.consume_rate

with open("io/4_RENTCARS.inp", "r") as f:
    N, M = map(int, f.readline().split(" "))
    distances = tuple(map(int, f.readline().split(" ")))
    consume_rates = tuple(map(int, f.readline().split(" ")))

sorted_distances = sorted(distances)
sorted_consume_rates = sorted(consume_rates, reverse=True)

def get_index(indexes: set, arr, val: int) -> int:
    at = 0
    index = arr.index(val, at)
    while index in indexes:
        at = index + 1
        index = arr.index(val, at)
    indexes.add(index)
    return index

total = 0
cars, cache_distances, cache_consume_rates = [], set(), set()
for i in range(N):
    consume_rate = sorted_consume_rates.pop()
    distance = sorted_distances.pop()

    distance_order = get_index(cache_distances, distances, distance)
    consume_rate_index = get_index(cache_consume_rates, consume_rates, consume_rate)

    selected_car = SelectedCar(distance, consume_rate, consume_rate_index, distance_order)
    total += selected_car.get_cost()
    cars.append(selected_car)

with open("io/4_RENTCARS.out", "w") as f:
    f.write(f"{total}\n")
    f.write(" ".join([str(car.index + 1) for car in sorted(cars)]))