f = open("day3.txt","r")
import math

#part 1
def priority(c):
  if not c.isupper(): return ord(c)-96
  else: return ord(c)-38

priorities = []

rucksacks = f.read().split()
for i in rucksacks:
  first = i[0:math.floor((len(i)/2))]
  second = i[math.floor(len(i)/2):len(i)]
  for x in first:
    if x in second:
      priorities.append(priority(x))
      break

print(sum(priorities))

# part 2
groupMarker = 0
priorities = []
for i in range(math.floor(len(rucksacks)/3)):
  group = rucksacks[groupMarker:groupMarker+3]
  combined = [set(group[0]), set(group[1]), set(group[2])]
  x = min(combined[0].intersection(combined[1],combined[2]))
  priorities.append(priority(x))
  groupMarker += 3

print(sum(priorities))