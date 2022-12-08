f = open("day7.txt","r")

# part 1
commands = f.read().splitlines()
dirMap = {}
currentDir =""
pathHistory = []

# construct map of all directories and their files
for c in commands:
  if c.split()[0] == '$' and c.split()[1] == 'cd' and c.split()[2] != '..':
    pathHistory.append(currentDir)
    currentDir = currentDir + " " + c.split()[2]
    dirMap[currentDir] = []
  elif c.split()[0].isnumeric():
    dirMap[currentDir].append(int(c.split()[0]))
  elif c.split()[0] == 'dir':
    dirMap[currentDir].append(c.split()[1])
  elif c.split()[0] == '$' and c.split()[1] == 'cd' and c.split()[2] == '..':
    currentDir = pathHistory.pop()

# recursively replace directories for their sizes
def getSize(dir):
  if all(isinstance(i, int) for i in dirMap[dir]):
    return sum(dirMap[dir])
  else:
    for f in dirMap[dir]:
      if not isinstance(f, int):
        dirMap[dir][dirMap[dir].index(f)] = getSize(dir + " " + f)
    return sum(dirMap[dir])


# add all the directories with sizes less than or equal to 100000
total = 0
for i in dirMap:
  if getSize(i) <= 100000:
    total += getSize(i)

print(total)

# part 2
smallest = 70000000
toDelete = 30000000 - (70000000 - getSize(" /"))
for i in dirMap:
  if getSize(i) >= toDelete and getSize(i) < smallest:
    smallest = getSize(i)

print(smallest)