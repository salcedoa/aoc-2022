f = open("day4.txt","r")

# part 1
import re
pairs = f.read().split()
contained = 0

for p in pairs:
  nums = list(map(lambda x: int(x),re.split(",|-",p)))
  if (nums[0] >= nums[2] and nums[1] <= nums[3]) or (nums[2] >= nums[0] and nums[3] <= nums[1]): 
    contained += 1

print(contained)

# part 2
contained = 0
for p in pairs:
  nums = list(map(lambda x: int(x),re.split(",|-",p)))
  firstRange = set(range(nums[0], nums[1]+1))
  secondRange = set(range(nums[2], nums[3]+1))
  
  if firstRange.intersection(secondRange):
    contained += 1

print(contained)