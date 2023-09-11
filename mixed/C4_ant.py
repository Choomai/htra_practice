n, l = [int(elem) for elem in input().split()]
class Ant:
    def __init__(self, weight: int, pos: float, direction):
        self.weight = weight
        self.pos = pos
        self.direction = direction
    
    def move(self, step):
        if self.pos != -1: self.pos += step * self.direction
    def drop(self):
        item_weight = self.weight
        self.weight = 0
        self.pos = -1
        return item_weight
    def rotate(self): self.direction *= -1

Ants = []
base_1, base_2 = 0,0
time = -0.5
for _ in range(n): Ants.append(Ant(*[int(elem) for elem in input().split()]))

total_weight = sum([ant.weight for ant in Ants])
need_weight_b1 = total_weight // 2
need_weight_b2 = total_weight - need_weight_b1

while base_1 != need_weight_b1 and base_2 != need_weight_b2:
    time += .5
    for ant in Ants:
        if ant.pos == 0: base_1 += ant.drop()
        elif ant.pos == l: base_2 += ant.drop()
        else: ant.move(.5)
    ants_pos = [ant.pos for ant in Ants]
    pos_to_check = set(ants_pos)
    if len(pos_to_check) == len(ants_pos): continue
    for pos in pos_to_check:
        indexes = [i for i, e in enumerate(ants_pos) if e == pos]
        if len(indexes) == 1: continue
        else:
            for index in indexes: Ants[index].rotate()

print(time)