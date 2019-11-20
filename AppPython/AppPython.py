M = 0;
с = 0;
List = [];
Element = "";
Dict = {};

with open("_.txt") as inf:
    for line in inf:
        List = List + line.split();


for i in range(len(List)):
    if (List[i].lower() in Dict):
        Dict[List[i]] += 1;
    elif (List[i].lower() not in Dict):
        Dict[List[i]] = 1;

maximum = max(Dict, key=Dict.get)  # Just use 'min' instead of 'max' for minimum.
print(maximum, Dict[maximum])

print(Dict);


##m = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9']];
##res = [];
###f = True;
###x = 0;
###while f:
###    s = list(input().split());
###    if (x == 0):
###        x = len(s);
###    if (s != ["end"]):
###        m.append(s);
###    else: 
###        f = False;
###        y = len(m);    

##for i in range(3):
##    for j in range(3):
##        if (i == 0 and j == 0):
##            res.append(sum([int(m[i + 1][j]), int(m[-1][j]), int(m[i][-1]), int(m[i][j + 1])]));
##        elif (i == 0 and j == (-1)):
##            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][-1]), int(m[i][j + 1])]));
##        elif (i == (-1) and j == 0):
##            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][-1])]));
##        elif (i == -1 and j == (-1)):
##            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][0]), int(m[i][j - 1])]));
##        elif (i == 1 and (j != 0 or j != (-1))):
##            res.append(sum([int(m[i + 1][j]), int(m[-1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
##        elif (i == (-1) and (j != 0 or j != (-1))):
##            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
##        elif ((i != 1 or i != (-1)) and j == 0):
##            res[i][j] = sum([m[i + 1][j], m[i - 1][j], m[i][j + 1], m[i][-1]]);
##        elif ((i != 1 or i != (-1)) and j != (-1)):
##            res.append(sum([int(m[i + 1][j]), int(m[i - 1][j]), int(m[i][0]), int(m[i][j - 1])]));
##        else:
##            res.append(sum([int(m[i + 1][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
##print(x, y);