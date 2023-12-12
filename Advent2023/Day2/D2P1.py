with open ("Day2\Input.txt", "r") as file:
  limit = {"red": 12, "blue": 14, "green": 13}
  total = 0
  gameColors = {}
  for line in file.readlines():
    grabs = line.count(";")
    gameNumber = line[line.find(" ") + 1: line.find(":")]
    line = line[line.find(":") + 2:]
    gameColors.update({gameNumber: {"red": 0, "blue": 0, "green": 0}})
    while len(line) != 0:
      if (line.count(";") > 0):
        grab = line[:line.find(";")]
        line = line[line.find(";") + 1:]
      else:
        grab = line
        line = ""
      grabbedBalls = grab.split(",")
      for item in grabbedBalls:
        item = item.strip()
        color = item[item.find(" ") + 1:]
        number = item[0:item.find(" ")]
        if (gameColors.get(gameNumber).get(color) < int(number)):
          gameColors.get(gameNumber).update({color: int(number)})
  for Num in gameColors.keys():
    fit = True
    for color in gameColors.get(Num).keys():
      if gameColors.get(Num).get(color) > limit.get(color):
        fit = False
    if fit:
      total += int(Num)
  print(total)
