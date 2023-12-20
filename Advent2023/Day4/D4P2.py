with open ("Advent2023\Day4\Input.txt", "r") as file:
  total = 0
  cardToCopies = {}
  totalCards = {}
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
    cardToCopies.update({cardNumber: [i for i in range(cardNumber + 1, cardNumber + matching + 2)]})
    totalCards.update({cardNumber: 1})
  print(cardToCopies)
  print(totalCards)
  for key in totalCards.keys():
    for i in range(totalCards.get(key)):
      for copy in cardToCopies.get(key):
        totalCards.update({copy: totalCards.get(copy) + 1})
  print(totalCards)
  for key in totalCards.keys():
    total += totalCards.get(key)
  print(total)
  #   cardToCopies.update({cardNumber: totalCards})
  #   totalCards.append(cardNumber)
  # for card in totalCards:
  #   print(totalCards)
  #   print(cardToCopies)
  #   totalCards.append(copy for copy in cardToCopies.get(card) if len(cardToCopies.get(card)) > 0)