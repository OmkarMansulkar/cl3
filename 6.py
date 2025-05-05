from collections import defaultdict

def mapper(text):
    # Split by sentence-ending punctuation
    return [("sentence", 1) for s in text if s in ".!?"]

def reducer(pairs):
    count = defaultdict(int)
    for k, v in pairs: count[k] += v
    return count

with open("input.txt") as f:
    data = f.read()

print("Sentence Count:")
for k, v in reducer(mapper(data)).items():
    print(f"{k}: {v}")
