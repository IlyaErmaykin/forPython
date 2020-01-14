n = int(input());
x = 0;
y = 0;

for play in range(n):
    a = input().split();
    if (a[0].lower() == "север"):
        y = y + int(a[1]);
    elif (a[0].lower() == "восток"):
        x = x + int(a[1]);
    elif (a[0].lower() == "юг"):
        y = y - int(a[1]);
    else:
        x = x - int(a[1]);

print(x, y);