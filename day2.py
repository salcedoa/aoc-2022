f = open("day2.txt","r")

# part 1
scoreValues = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

total = []

rounds = f.read().split('\n')
rounds.remove('')
for r in rounds:
  score = scoreValues[r[2]]
  if r in ['A Z','B X','C Y']:
    total.append(score)
  elif r in ['A X','B Y','C Z']:
    total.append(score + 3)
  else:
    total.append(score + 6)
  score = 0

print(sum(total))

# part 2
loss = { 'A':3, 'B':1, 'C':2 }
win = { 'A':2, 'B':3, 'C':1 }
draw = { 'A':1, 'B':2, 'C':3 }

total = []
for r in rounds:
  if r[2] == 'X': total.append(loss[r[0]])
  elif r[2] == 'Z': total.append(win[r[0]] + 6)
  else: total.append(draw[r[0]] + 3)

print(sum(total))