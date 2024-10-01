with open("io/2_roundtrip.inp", "r") as f:
    N, P = map(int, f.readline().split())
    trip = ""
    for _ in range(P): trip += f.readline()[:3:2]

def generate_trip(max_node: int) -> str:
    base_str = list(map(str, range(max_node)))
    base_str.append("0")
    for i in range(1, max_node): base_str[i] = base_str[i] * 2
    return "".join(base_str)

print(generate_trip(N) in trip)