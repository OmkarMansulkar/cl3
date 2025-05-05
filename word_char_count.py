from collections import defaultdict

def mapper(text, by="word"):
    return [(c,1) for c in (text.split() if by=="word" else text.replace(" ","").replace("\n",""))]

def reducer(pairs):
    count = defaultdict(int)
    for k, v in pairs: count[k] += v
    return count

with open("input.txt") as f:
    data = f.read()

print("Character Count:")
for k,v in reducer(mapper(data, "char")).items(): print(f"{k}: {v}")

print("\nWord Count:")
for k,v in reducer(mapper(data, "word")).items(): print(f"{k}: {v}")
