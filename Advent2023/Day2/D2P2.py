with open ("Day2\Input.txt", "r") as file:
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
    start = 1
    for color in gameColors.get(Num).keys():
      start = start * gameColors.get(Num).get(color)
    total += start
  print(total)
