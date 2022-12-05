f = open("day5.txt","r")

# part 1
from collections import deque
import re

inputSections = f.read().split('\n\n')
crateMap = inputSections[0]
instructions = inputSections[1]

numOfStacks = int(crateMap.split()[-1])

# populate initial stacks
def initializeStacks():
  stacks = {c:deque() for c in range(numOfStacks)}
  lines = crateMap.splitlines()

  x = 0
  y = 3
  for s in range(numOfStacks):
    for c in range(numOfStacks):
      crate = lines[c][x:y]
      if bool(re.match("\S",crate)):
        stacks[s].appendleft(crate)
    x += 4
    y += 4
  return stacks

stacks = initializeStacks()

# perform instructions
for i in instructions.splitlines():
  nums = re.split("move | to | from ",i)
  for i in range(int(nums[1])):
    stacks[int(nums[3])-1].append(stacks[int(nums[2])-1].pop())

# get last letters
letters = []
for s in range(numOfStacks):
  if stacks[s]: letters.append(stacks[s].pop())

letters = "".join(letters)
print("".join([x for x in letters if x.isalnum()]))


# part 2
stacks = initializeStacks()

# perform instructions
for i in instructions.splitlines():
  nums = re.split("move | to | from ",i)
  if nums[1] == 1:
    stacks[int(nums[3])-1].append(stacks[int(nums[2])-1].pop())
  else:
    temp = deque()
    for i in range(int(nums[1])):
      temp.append(stacks[int(nums[2])-1].pop())
    for i in range(int(nums[1])):
      stacks[int(nums[3])-1].append(temp.pop())

# get last letters
letters = []
for s in range(numOfStacks):
  if stacks[s]: letters.append(stacks[s].pop())

letters = "".join(letters)
print("".join([x for x in letters if x.isalnum()]))