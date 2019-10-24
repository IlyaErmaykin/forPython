a = [int(i) for i in input().split()];
n = int(input());
f = False;

for i in range(len(a)):
    if(a[i] == n):
        print(i, end=" ");
        f = True;
    else:
        continue;
if(not f):
    print("Отсутствует");