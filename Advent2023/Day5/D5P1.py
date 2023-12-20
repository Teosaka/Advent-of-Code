def addMapping(string, map):
  nums = string.split()
  keyObj = int(nums[1].strip())
  mapObj = int(nums[0].strip())
  mapRange = int(nums[2].strip()) - 1
  map.update({keyObj: [mapObj, keyObj + mapRange]})

def checkMap(num, map):
  for key in map.keys():
    if key <= num <= map.get(key)[1]:
      difference = num - key
      return map.get(key)[0] + difference
  return num

def checkSeed(seed):
  print("seed:", seed)
  soil = checkMap(seed, s2sMap)
  print("soil:", soil)
  fertilizer = checkMap(soil, s2fMap)
  print("fert:", fertilizer)
  water = checkMap(fertilizer, f2wMap)
  print("water:", water)
  light = checkMap(water, w2lMap)
  print("light:", light)
  temperature = checkMap(light, l2tMap)
  print("temp:", temperature)
  humidity = checkMap(temperature, t2hMap)
  print("hum:", humidity)
  location = checkMap(humidity, h2lMap)
  print("loc:", location)
  return location

with open ("Advent2023\Day5\Input.txt", "r") as file:
  lowest = -1
  seeds = []
  lines = file.readlines()
  s2s = lines.index("seed-to-soil map:\n")
  s2sMap = {}
  s2f = lines.index("soil-to-fertilizer map:\n")
  s2fMap = {}
  f2w = lines.index("fertilizer-to-water map:\n")
  f2wMap = {}
  w2l = lines.index("water-to-light map:\n")
  w2lMap = {}
  l2t = lines.index("light-to-temperature map:\n")
  l2tMap = {}
  t2h = lines.index("temperature-to-humidity map:\n")
  t2hMap = {}
  h2l = lines.index("humidity-to-location map:\n")
  h2lMap = {}
  for line in lines:
    if lines.index(line)  == 0:
      seedLine = line[line.find(":") + 1: -1]
      for num in seedLine.split():
          seeds.append(int(num.strip()))
    elif (s2s < lines.index(line) < s2f - 1):
      addMapping(line, s2sMap)
    elif (s2f < lines.index(line) < f2w - 1):
      addMapping(line, s2fMap)
    elif (f2w < lines.index(line) < w2l - 1):
      addMapping(line, f2wMap)
    elif (w2l < lines.index(line) < l2t - 1):
      addMapping(line, w2lMap)
    elif (l2t < lines.index(line) < t2h - 1):
      addMapping(line, l2tMap)
    elif (t2h < lines.index(line) < h2l - 1):
      addMapping(line, t2hMap)
    elif (h2l < lines.index(line)):
      addMapping(line, h2lMap)
  for seed in seeds:
    seedLoc = checkSeed(seed)
    if seedLoc < lowest or lowest < 0:
      lowest = seedLoc
  print(lowest)

