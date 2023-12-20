with open ("Advent2023\\Day4\\Input.txt", "r") as file:
  total = 0
  for line in file.readlines():
    cardNumber = int(line[line.find(" ") + 1: line.find(":")])
    winning = line[line.find(":") + 2: line.find("|") - 1]
    have = line[line.find("|") + 2:]
    winningNumbers = winning.split()
    haveNumbers = have.split()
    matching = -1
    for num in haveNumbers:
      if num in winningNumbers:
        matching += 1
    if matching >= 0:
      total += 2 ** matching
  print(total)