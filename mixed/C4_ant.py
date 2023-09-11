n, l = [int(elem) for elem in input().split()]
class Ant:
    def __init__(self, weight: int, pos: float, direction):
        self.weight = weight
        self.pos = pos
        self.direction = direction
    
    def move(self, step): self.pos += step * self.direction
    def drop(self):
        item_weight = self.weight
        self.weight = 0
        self.pos = -1
        return item_weight
    def rotate(self): self.direction *= -1

Ants = []
base_1, base_2 = 0,0
time = 0
for _ in range(n): Ants.append(Ant(*[int(elem) for elem in input().split()]))

total_weight = sum([ant.weight for ant in Ants])
if total_weight % 2 == 1: need_weight_b1 = total_weight // 2
need_weight_b2 = total_weight - need_weight_b1

while base_1 != need_weight_b1 and base_2 != need_weight_b2:
    time += 1
    for ant in Ants: 
        if ant.pos == 0: base_1 += ant.drop()
        elif ant.pos == l: base_2 += ant.drop()
        else: ant.move(.5)
