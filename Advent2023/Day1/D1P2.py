with open("Advent2023\Day1\Input.txt", "r") as file:
  numToString = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
  total = 0
  for line in file.readlines():
    firstString = len(line)
    lastString = -1
    firstWordNum = 0
    lastWordNum = 0
    numString = ""
    front = True
    end = True
    for word in numToString.keys():
      if line.find(word) >= 0 and line.find(word) < firstString:
        firstString = line.find(word)
        firstWordNum = numToString.get(word)
      if line.rfind(word) > lastString:
        lastString = line.rfind(word)
        lastWordNum = numToString.get(word)
    for i in range (firstString):
      if line[i].isnumeric() and front:
        numString = line[i] + numString
        front = False
    for j in range (len(line) - 1, lastString, -1):
      if line[j].isnumeric() and end:
        numString += line[j]
        end = False
    if front:
      numString = str(firstWordNum) + numString
    if end:
      numString += str(lastWordNum)
    total += int(numString)
  print(total)
