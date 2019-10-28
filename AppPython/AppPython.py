def modify_list(l):
    i = 0;
    while (i < len(l)):
        if (l[i] % 2 == 0):
            l[i] = (l[i] // 2);
            i += 1;
        else:
            l.remove(l[i]);
    return;

l = [1, 2, 3, 4, 5, 6]
print(modify_list(l))  # None
print(l)               # [1, 2, 3]
modify_list(l)
print(l)               # [1]

l = [10, 5, 8, 3]
modify_list(l)
print(l)

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