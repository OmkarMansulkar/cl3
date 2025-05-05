import os
import re
import pandas as pd

os.listdir()

def mapper(review):
    review = review.strip()
    review = review.lower()
    review = re.findall("[a-z]+", review)
    return review

def reduce(review):
    word_count = {}
    for word in review:
        word_count[word] = review.count(word)
    return word_count

def map_reduce(input):
    with open(input, "r") as file:
        review = file.read()
        
    mapped = mapper(review)
    reducer = reduce(mapped)
    
    x1, x2 = [], []
    for word, count in reducer.items():
        x1.append(word)
        x2.append(count)
    return x1, x2

y1, y2 = map_reduce("input.txt")

dict1 = {"count":y2}
pd.DataFrame(dict1, index=y1)

