f = open("day1.txt","r")

# part 1
calorieList = f.read().split("\n")
total = 0
caloriesPerElf = []
for i in calorieList:
  if i == '': 
    caloriesPerElf.append(int(total))
    total = 0
  else: 
    total += int(i)

print(caloriesPerElf.index(max(caloriesPerElf)) + 1)
print(max(caloriesPerElf))

# part 2
x = sorted(caloriesPerElf)
print(x[-1] + x[-2] + x[-3])