# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if (key in d):
        d.setdefault(key, []).append(value);
    elif(key * 2  in d):
        d.setdefault(key * 2, []).append(value);
    else :
        d[key * 2] = [value];
    return;
# не добавляйте кода вне функции

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  
#print(update_dictionary(d, 0, -5))  # none
#print(d)                            # {2: [-1]}
#update_dictionary(d, 1, -1)
#print(d)                            # {2: [-1, -2]}
#update_dictionary(d, 2, -2)
#print(d)                   
#update_dictionary(d, 3, -3)
#print(d)                            # {2: [-1, -2, -3]}
#m = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9']];
#res = [];
##f = True;
##x = 0;
##while f:
##    s = list(input().split());
##    if (x == 0):
##        x = len(s);
##    if (s != ["end"]):
##        m.append(s);
##    else: 
##        f = False;
##        y = len(m);    

#for i in range(3):
#    for j in range(3):
#        if (i == 0 and j == 0):
#            res.append(sum([int(m[i + 1][j]), int(m[-1][j]), int(m[i][-1]), int(m[i][j + 1])]));
#        elif (i == 0 and j == (-1)):
#            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][-1]), int(m[i][j + 1])]));
#        elif (i == (-1) and j == 0):
#            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][-1])]));
#        elif (i == -1 and j == (-1)):
#            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][0]), int(m[i][j - 1])]));
#        elif (i == 1 and (j != 0 or j != (-1))):
#            res.append(sum([int(m[i + 1][j]), int(m[-1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
#        elif (i == (-1) and (j != 0 or j != (-1))):
#            res.append(sum([int(m[0][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
#        elif ((i != 1 or i != (-1)) and j == 0):
#            res[i][j] = sum([m[i + 1][j], m[i - 1][j], m[i][j + 1], m[i][-1]]);
#        elif ((i != 1 or i != (-1)) and j != (-1)):
#            res.append(sum([int(m[i + 1][j]), int(m[i - 1][j]), int(m[i][0]), int(m[i][j - 1])]));
#        else:
#            res.append(sum([int(m[i + 1][j]), int(m[i - 1][j]), int(m[i][j + 1]), int(m[i][j - 1])]));
#print(x, y);