f = open("day8.txt","r")

# part 1
grid = f.read().splitlines()
x = len(grid[0])
y = len(grid)
perimeter = 2 * (x + y) - 4
visibleTrees = perimeter

# return true if there are any trees taller or the same height as the current tree
def checkLeft(row, column):
  return bool([int(i) for i in grid[row][0:column] if int(i) >= int(grid[row][column])])

def checkRight(row, column):
  return bool([int(i) for i in grid[row][column+1:x] if int(i) >= int(grid[row][column])])

def checkAbove(row, column):
  up = [int(i[column]) for i in grid[0:row]]
  return bool([i for i in up if i >= int(grid[row][column])])

def checkBelow(row, column):
  down = [int(i[column]) for i in grid[row+1:y]]
  return bool([i for i in down if i >= int(grid[row][column])])

for c in range(1,x-1):
  for r in range(1,y-1):
    if not checkLeft(r,c) or not checkRight(r,c) or not checkAbove(r,c) or not checkBelow(r,c):
      visibleTrees += 1

print(visibleTrees)

# part 2
def visibleLeft(row,column): 
  view = [int(i) for i in reversed(grid[row][0:column])]
  shorter = 0
  for i in view:
    if i < int(grid[row][column]): shorter += 1
    else: 
      shorter += 1
      break
  return shorter

def visibleRight(row,column): 
  view = [int(i) for i in grid[row][column+1:x]]
  shorter = 0
  for i in view:
    if i < int(grid[row][column]): shorter += 1
    else: 
      shorter += 1
      break
  return shorter

def visibleUp(row,column): 
  view = reversed([int(i[column]) for i in grid[0:row]])
  shorter = 0
  for i in view:
    if i < int(grid[row][column]): shorter += 1
    else:
      shorter += 1
      break
  return shorter

def visibleDown(row,column): 
  view = [int(i[column]) for i in grid[row+1:y]]
  shorter = 0
  for i in view:
    if i < int(grid[row][column]): shorter += 1
    else:
      shorter += 1
      break
  return shorter

best = 0
for c in range(1,x-1):
  for r in range(1,y-1):
    score = visibleLeft(r,c) * visibleRight(r,c) * visibleUp(r,c) * visibleDown(r,c)
    if score > best: best = score

print(best)