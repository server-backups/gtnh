f1 = open("5a71afae-160c-38ea-a990-deac83e26fbf.json")
f2 = open("3f73bdc4-9b7f-409d-875c-c90e84c3513d.json")

import json

d1 = json.load(f1)
d2 = json.load(f2)

del d1["achievement.exploreAllBiomes"]
print(d1)

for key in d1:
    d2[key] += d1[key]

f = open("test.json", "w")
json.dump(d2, f)
