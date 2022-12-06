f = open("day6.txt","r")

# part 1
chars = f.read()

searched = []
for i in range(len(chars)-4):
  searched = []
  for x in range(4):
    if chars[(i+4) - x] not in searched: searched.append(chars[(i+4) - x])
    else: break
  if len(searched) == 4:
    print(i+5)
    print(list(reversed(searched)))
    break

# part 2
searched = []
for i in range(len(chars)-14):
  searched = []
  for x in range(14):
    if chars[(i+14) - x] not in searched: searched.append(chars[(i+14) - x])
    else: break
  if len(searched) == 14:
    print(i+15)
    print(list(reversed(searched)))
    break