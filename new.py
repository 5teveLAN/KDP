namelist = []
unitlist = []
dic = {}
cnt = 0
# while True:
#     inp = input()
#     if inp == "NO":  break
while True:
    inp = input()
    if inp == "任教學校" or inp == "":
        continue
    if inp == "NO":
        break
    unitlist.append(inp)
    cnt+=1
while True:
    inp = input()
    if inp == "參賽人員" or inp == "":
        continue
    if inp == "NO":
        break
    names = inp.split()
    namelist.append(names)
        
for i in range(0, cnt):
    for name in namelist[i]:
        dic[name] = set()
for i in range(0, cnt):
    for name in namelist[i]:
        dic[name].add(unitlist[i])

for result in dic:
    if len(dic[result]) <= 1:
        continue
    print(result,end = ' ')
    for unit in dic[result]:
        print(unit, end=' ')
    print()