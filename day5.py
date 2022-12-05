f = open("test.txt","r")

# part 1
from collections import deque
import re

inputSections = f.read().split('\n\n')
crateMap = inputSections[0]
instructions = inputSections[1]

numOfStacks = int(crateMap.split()[-1])

stacks = {c:deque() for c in range(numOfStacks)}

def getInstructionsList(ins):
  return list(map(lambda x: int(x),re.split("move | from | to ",ins)))

line = crateMap.splitlines()
print(line[0][0:3])
print(line[0][4:7])
print(bool(re.match("\s",line[0][0:3])))

x = 0
y = 3

for i in range(numOfStacks):
  crate = line[i][x:y]
  if bool(re.match("\S",crate)):
    stacks[i].appendleft(crate)
    
  x += 4
  y += 4