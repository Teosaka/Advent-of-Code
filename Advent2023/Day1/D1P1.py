with open("Day1\Input.txt", "r") as file:
  total = 0
  for line in file.readlines():
    numString = ""
    front = True
    end = True
    for i in range (len(line)):
      if line[i].isnumeric() and front:
        numString = line[i] + numString
        front = False
      if line[len(line)- i - 1].isnumeric() and end:
        numString += line[len(line) - i - 1]
        end = False
      if not front and not end:
        break
    total += int(numString)
  print(total)
