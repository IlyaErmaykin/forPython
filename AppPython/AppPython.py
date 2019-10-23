#Переделать
a = [int(i) for i in input().split()];
s = 0;
a.sort();
a.append('0');
n = a[0];
for i in a:
    if n != i:    
        if s >= 2:
            print(str(n), end=" ");
        s = 0;
        n = i;
    s += 1;