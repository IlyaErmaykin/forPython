a = int(input());
b = int(input());
c = int(input());
d = int(input());
print(" ", end=" ");
for x in range (c,d + 1):
    print(x, end=" ");
    x += 1;
    continue;
print();

for i in range (a, b + 1):
    for j in range (c - 1, d + 1):
        if (j == c - 1):
            print(i, end=" ");
            continue;
        print(i * j, end=" ");
        j += 1;
    print();
    i += 1;
        

